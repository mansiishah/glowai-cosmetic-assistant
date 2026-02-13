import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from data.products import products

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="text-embedding-3-small"
)

def build_vector_store():
    documents = []

    for product in products:
        content = f"""
        Name: {product['name']}
        Category: {product['category']}
        Price: {product['price']}
        Skin Type: {product.get('skin_type', '')}
        Finish: {product.get('finish', '')}
        Description: {product['description']}
        """

        documents.append(
            Document(
                page_content=content,
                metadata={"id": product["id"]}
            )
        )

    return FAISS.from_documents(documents, embeddings)

vector_store = build_vector_store()

def retrieve_products(query, k=3):
    return vector_store.similarity_search(query, k=k)
