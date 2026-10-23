products = {
    "laptop": 75000,
    "phone": 30000,
    "headphones": 5000,
    "keyboard": 3500,
    "mouse": 2000
}

cart = []

def show_products():
    for name, price in products.items():
        print(f"{name.capitalize()} - Ksh {price}")

def add_to_cart():
    item = input("Enter product name: ").lower()
    if item in products:
        cart.append(item)
        print(f"{item.capitalize()} added to cart.")
    else:
        print("Product not found.")

def show_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        total = 0
        for item in cart:
            print(f"{item.capitalize()} - Ksh {products[item]}")
            total += products[item]
        print(f"Total: Ksh {total}")

while True:
    print("\n===== SHOPPING CART =====")
    print("1. View Products\n2. Add Product\n3. View Cart\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        show_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        show_cart()
    elif choice == "4":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice.")