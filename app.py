import streamlit as st
from dotenv import load_dotenv
from data.products import products
from utils.filter import filter_products
from ai.assistant import get_ai_response

load_dotenv()

st.set_page_config(page_title="GlowAI Cosmetic Assistant", page_icon="💄")
st.title("💄 GlowAI Cosmetic Assistant")

# Session state
if "cart" not in st.session_state:
    st.session_state.cart = []

if "messages" not in st.session_state:
    st.session_state.messages = []

if "recommended_product_ids" not in st.session_state:
    st.session_state.recommended_product_ids = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Ask about our products...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    filtered = filter_products(user_input, products)

    ai_response = get_ai_response(
        user_input,
        filtered,
        st.session_state.messages
    )

    assistant_message = ai_response.get("message", "")

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_message}
    )

    with st.chat_message("assistant"):
        st.write(assistant_message)

    st.session_state.recommended_product_ids = ai_response.get(
        "recommended_product_ids",
        []
    )

# Add to cart buttons
for product_id in st.session_state.recommended_product_ids:

    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if product:
        if st.button(
            f"Add {product['name']} to cart",
            key=f"add_{product_id}"
        ):
            st.session_state.cart.append(product)
            st.success(f"Added {product['name']} to cart!")

# Cart display
st.subheader("🛒 Cart")

total = 0

if st.session_state.cart:
    for item in st.session_state.cart:
        st.write(f"{item['name']} - ₹{item['price']}")
        total += item["price"]

    st.write(f"### Total: ₹{total}")
else:
    st.write("Your cart is empty.")
