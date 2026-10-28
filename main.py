# Simulated database of products
PRODUCT_DATABASE = {
    "123456789": {
        "name": "Wireless Mouse",
        "price": 25.00,
        "discount_percent": 10
    },
    "987654321": {
        "name": "Mechanical Keyboard",
        "price": 75.50,
        "discount_percent": 15
    },
    "456789123": {
        "name": "USB-C Charging Cable",
        "price": 12.99,
        "discount_percent": 0
    }
}

def get_product_info(chip_id):
    """Looks up the product in the database using its chip ID."""
    return PRODUCT_DATABASE.get(chip_id, None)

def main():
    print("--- POS Software Started ---")
    cart = []
    
    # Simulate scanning items in a loop
    while True:
        print("\nEnter product code (or type 'done' to finish shopping):")
        user_input = input("Scan/Enter Code: ").strip()
        
        if user_input.lower() == 'done':
            break
            
        product = get_product_info(user_input)
        if product:
            cart.append(product)
            print(f"Added to cart: {product['name']} - ${product['price']:.2f}")
        else:
            print("❌ Product not found. Please try again.")
            
    # Display current cart summary
    print("\n--- Current Cart Summary ---")
    if not cart:
        print("No items added.")
    else:
        for item in cart:
            print(f"- {item['name']}: ${item['price']:.2f}")

if __name__ == "__main__":
    main()