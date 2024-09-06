# Objective:

# Pass the shopping cart list to functions by reference.
# Add items to the cart, update quantities, and remove items from the cart.
# Ensure changes made to the cart in the functions reflect in the main program.

# Pass by Reference: In Python, lists are mutable, and when passed to functions, they are passed by reference.


shopping_cart = [
    {
        'name': 'oat',
        'quantity': 10,
        'price': 1.5
    },
    {
        'name': 'apple',
        'quantity': 5,
        'price': 0.75
    },
    {
        'name': 'banana',
        'quantity': 8,
        'price': 0.5
    }
]


def add_item(item_add_cart: dict):
    shopping_cart.append(item_add_cart)


def update_cart(cart: list, item_name: str, new_quantity: int):
    for i in cart:
        if i['name'] == item_name:
            i['quantity'] = new_quantity
            return

    print(f"{item_name} not found in the cart")


def remove_item(cart: list, item_name: str):
    for i in cart:
        if i['name'] == item_name:
            cart.remove(i)
            print(f"{item_name} removed from the cart")
            return

    print(f"{item_name} not found in the cart")


def calc_total_price(cart: list):
    if not cart:
        print("Cart is empty")
        return 0
    total = 0
    for i in cart:
        total += i['price'] * i['quantity']
    return total


def display_cart(cart: list):
    if not cart:
        print("Cart is empty")
        return
    for i in cart:
        print(f"Name: {i['name']}, quantity: {i['quantity']}, price: ${i['price']}")


# Create a simple menu-driven interface for the user.
while True:
    print("\nShopping Cart Menu:")
    print("1. Add item")
    print("2. Update item quantity")
    print("3. Remove item")
    print("4. Display cart")
    print("5. Calculate total price")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter item name: ")
        quantity = input("Enter item quantity: ")
        price = input("Enter item price: ")

        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            print("Invalid quantity or price. Please enter numbers.")
            continue

        item = {
            'name': name,
            'quantity': quantity,
            'price': price
        }

        add_item(item)
        print("Item added successfully")

    elif choice == '2':
        name = input("Enter item name to update: ")
        quantity = input("Enter new quantity: ")

        try:
            quantity = int(quantity)
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        update_cart(shopping_cart, name, quantity)

    elif choice == '3':
        name = input("Enter item name to remove: ")

        remove_item(shopping_cart, name)

    elif choice == '4':
        display_cart(shopping_cart)

    elif choice == '5':
        total_price = calc_total_price(shopping_cart)
        print(f"Total price: ${total_price}")

    elif choice == '6':
        break
