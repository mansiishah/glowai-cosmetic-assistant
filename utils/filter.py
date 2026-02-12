def filter_products(user_input, products):
    user_input = user_input.lower().split()

    scored_products = []

    for product in products:
        score = 0

        fields = [
            product["name"].lower(),
            product["category"].lower(),
            product.get("skin_type", "").lower(),
            product.get("finish", "").lower(),
            product.get("description", "").lower()
        ]

        for word in user_input:
            for field in fields:
                if word in field:
                    score += 1

        if score > 0:
            scored_products.append((score, product))

    # Sort by score descending
    scored_products.sort(key=lambda x: x[0], reverse=True)

    # Return only products (remove score)
    return [p[1] for p in scored_products] if scored_products else products
