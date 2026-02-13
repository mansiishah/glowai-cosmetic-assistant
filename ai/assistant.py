import json
import os
from openai import OpenAI
from ai.rag import retrieve_products
from data.products import products

def get_ai_response(user_input, chat_history):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # 🔥 RAG Retrieval
    retrieved_docs = retrieve_products(user_input)

    filtered_products = []
    for doc in retrieved_docs:
        product_id = doc.metadata["id"]
        product = next(
            (p for p in products if p["id"] == product_id),
            None
        )
        if product:
            filtered_products.append(product)

    system_prompt = f"""
    You are a premium cosmetic shop assistant.
    Use ONLY the retrieved products below.

    Return STRICT JSON:

    {{
        "message": "response text",
        "recommended_product_ids": [list_of_ids_or_empty_list]
    }}

    Retrieved Products:
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
    except:
        return {
            "message": raw_output,
            "recommended_product_ids": []
        }
