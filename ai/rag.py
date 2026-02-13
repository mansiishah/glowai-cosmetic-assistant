import os
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from data.products import products

# Create embedding model
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

# Build once at startup
vector_store = build_vector_store()

def retrieve_products(query, k=3):
    results = vector_store.similarity_search(query, k=k)
    return results
