def filter_products(user_input, products):
    user_input = user_input.lower()
    filtered = []

    for product in products:
        if (
            product["category"].lower() in user_input
            or product["name"].lower() in user_input
            or product.get("skin_type", "").lower() in user_input
            or product.get("finish", "").lower() in user_input
        ):
            filtered.append(product)

    return filtered if filtered else products
