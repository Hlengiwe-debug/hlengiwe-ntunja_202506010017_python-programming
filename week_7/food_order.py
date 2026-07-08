def calculate_total(price, quantity):
    # Check for negative values
    if price < 0:
        return "invalid price"
    if quantity < 0:
        return "invalid quantity"
    # Valid input – multiply
    return price * quantity