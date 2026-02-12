import json
import os
from openai import OpenAI

def get_ai_response(user_input, filtered_products, chat_history):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    system_prompt = f"""
    You are a premium cosmetic shop assistant.
    Be elegant, friendly, and helpful.

    Use ONLY the provided products.
    Return STRICT JSON:

    {{
        "message": "response text",
        "recommended_product_id": product_id_or_null
    }}

    Products:
    {json.dumps(filtered_products, indent=2)}
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": system_prompt},
            *chat_history,
            {"role": "user", "content": user_input}
        ],
        temperature=0.3
    )

    return json.loads(response.output_text)
