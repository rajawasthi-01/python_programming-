cart = [
    {"id": 101, "name": "Laptop", "price": 55000,
     "qty": 1, "discount": 10},
    {"id": 102, "name": "Mouse", "price": 800,
     "qty": 2, "discount": 5},
    {"id": 103, "name": "Keyboard", "price": 1500,
     "qty": 1, "discount": 0}
]

def display_cart():
    for item in cart:
        print(item["id"], item["name"],
              "Price:", item["price"],
              "Quantity:", item["qty"])

def search_product():
    name = input("Enter product name: ").lower()

    for item in cart:
        if name in item["name"].lower():
            print("Product found:", item)
            return

    print("Product not found")

def add_product():
    name = input("Enter product name: ")
    price = int(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    cart.append({
        "id": len(cart) + 101,
        "name": name,
        "price": price,
        "qty": qty,
        "discount": 0
    })

    print("Product added successfully")

def generate_bill():
    total = 0
    discount_total = 0

    for item in cart:
        cost = item["price"] * item["qty"]
        discount = cost * item["discount"] / 100

        total += cost
        discount_total += discount

        print(item["name"], "Cost:", cost,
              "Discount:", discount)

    amount = total - discount_total

    if amount > 50000:
        amount = amount - amount * 0.05

    print("Total Bill:", total)
    print("Product Discounts:", discount_total)
    print("Final Amount:", amount)

while True:
    print("\n1. Display Products")
    print("2. Search Product")
    print("3. Add Product")
    print("4. Generate Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_cart()
    elif choice == "2":
        search_product()
    elif choice == "3":
        add_product()
    elif choice == "4":
        generate_bill()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")