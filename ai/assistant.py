import json
import os
from openai import OpenAI

def get_ai_response(user_input, filtered_products, chat_history):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    system_prompt = f"""
    You are a premium cosmetic shop assistant.
    Be elegant, friendly, and helpful.

    Use ONLY the provided products.

    Return STRICT JSON in this format:

    {{
        "message": "response text",
        "recommended_product_ids": [list_of_product_ids_or_empty_list]
    }}

    Do NOT include anything outside the JSON.
    Do NOT add explanations before or after JSON.

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
        temperature=0.2
    )

    raw_output = response.output_text.strip()

    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        # Safe fallback
        return {
            "message": raw_output,
            "recommended_product_ids": []
        }
