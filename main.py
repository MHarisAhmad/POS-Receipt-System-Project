from datetime import datetime

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
            
    # Check if cart is empty before generating receipt
    if not cart:
        print("\nNo items added. Exiting.")
        return

    # --- RECEIPT GENERATION & CALCULATIONS ---
    print("\n" + "=" * 35)
    print("           OFFICIAL RECEIPT         ")
    print("=" * 35)
    
    # Get current date and time
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Date: {formatted_date}")
    print("-" * 35)

    subtotal = 0.0
    total_discount = 0.0
    tax_rate = 0.05  # 5% tax rate

    # Loop through items in cart to calculate prices and print details
    for item in cart:
        price = item['price']
        discount_pct = item['discount_percent']
        
        # Calculate discount money saved on this item
        item_discount = price * (discount_pct / 100)
        final_item_price = price - item_discount
        
        # Add to running totals
        subtotal += price
        total_discount += item_discount
        
        print(f"{item['name']}")
        print(f"  Price: ${price:.2f} | Discount: {discount_pct}% (-${item_discount:.2f})")
        print(f"  Subtotal: ${final_item_price:.2f}")
        print("-" * 35)

    # Calculate final tax and grand total
    discounted_subtotal = subtotal - total_discount
    tax_amount = discounted_subtotal * tax_rate
    grand_total = discounted_subtotal + tax_amount

    # Print summary financials
    print(f"Subtotal:       ${subtotal:.2f}")
    print(f"Total Discount: -${total_discount:.2f}")
    print(f"Tax (5%):       ${tax_amount:.2f}")
    print("=" * 35)
    print(f"GRAND TOTAL:    ${grand_total:.2f}")
    print("=" * 35)
    print("      Thank you for shopping!       ")

if __name__ == "__main__":
    main()