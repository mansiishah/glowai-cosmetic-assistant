import streamlit as st
from dotenv import load_dotenv
from data.products import products
from utils.filter import filter_products
from ai.assistant import get_ai_response

# Load environment variables
load_dotenv()

st.set_page_config(page_title="GlowAI Cosmetic Assistant", page_icon="💄")
st.title("💄 GlowAI Cosmetic Assistant")

# ----------------------------
# Initialize Session State
# ----------------------------

if "cart" not in st.session_state:
    st.session_state.cart = []

if "messages" not in st.session_state:
    st.session_state.messages = []

if "recommended_product_id" not in st.session_state:
    st.session_state.recommended_product_id = None

# ----------------------------
# Display Chat History
# ----------------------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ----------------------------
# Chat Input
# ----------------------------

user_input = st.chat_input("Ask about our products...")

if user_input:

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Filter products before LLM call
    filtered = filter_products(user_input, products)

    # Call AI
    ai_response = get_ai_response(
        user_input,
        filtered,
        st.session_state.messages
    )

    assistant_message = ai_response["message"]

    # Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_message}
    )

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(assistant_message)

    # Save recommended product to session state
    st.session_state.recommended_product_id = ai_response.get(
        "recommended_product_id"
    )

# ----------------------------
# Add To Cart Button (Stable)
# ----------------------------


if st.session_state.recommended_product_id:

    product = next(
        (p for p in products if p["id"] == st.session_state.recommended_product_id),
        None
    )

    if product:
        if st.button(f"Add {product['name']} to cart"):
            st.session_state.cart.append(product)
            st.success("Added to cart!")
            st.session_state.recommended_product_id = None

# ----------------------------
# Cart Display
# ----------------------------

st.subheader("🛒 Cart")

total = 0

if st.session_state.cart:
    for item in st.session_state.cart:
        st.write(f"{item['name']} - ₹{item['price']}")
        total += item["price"]

    st.write(f"### Total: ₹{total}")
else:
    st.write("Your cart is empty.")