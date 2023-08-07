import json

MENU_FILE = "menu.json"

def save_menu(menu):
    with open(MENU_FILE, "w") as file:
        json.dump(menu, file)

def load_menu():
    try:
        with open(MENU_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def display_menu(menu):
    if not menu:
        print("The menu is empty.")
        return

    print("------ Menu ------")
    for item_id, (food, price, quantity, dine_in) in menu.items():
        total_price = price * quantity
        dine_in_status = "Dine-in" if dine_in else "Take-away"
        print(f"{item_id}. {food} - ${price:.2f} - Quantity: {quantity} -Take-away/Dine-in : {dine_in_status} - Total-Price: ${total_price:.2f}")
    print("------------------")

def add_item(menu):
    while True:
        food = input("Enter the name of the new food: ")
        if food.lower() == 'done':
            break

        price = float(input("Enter the price of the new food: "))
        quantity = int(input("Enter the quantity of the new food: "))
        print("Select an option for dine-in or take-away:")
        print("1. Dine-in")
        print("2. Take-away")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            dine_in = True
        elif choice == '2':
            dine_in = False
        else:
            print("Invalid choice. Assuming Take-away.")
            dine_in = False

        item_id = len(menu) + 1
        menu[item_id] = (food, price, quantity, dine_in)
        total_price = price * quantity
        print(f"{quantity} {food}(s) have been added to the menu. Total: ${total_price:.2f}")

        add_more = input("Do you want to add more food items? (yes/no): ").strip().lower()
        if add_more != 'yes':
            break

    save_menu(menu)  # Save the updated menu

def remove_item(menu):
    display_menu(menu)
    item_id = int(input("Enter the item ID of the food to remove: "))
    if item_id in menu:
        food, _, _, _ = menu.pop(item_id)
        print(f"{food} has been removed from the menu.")
    else:
        print("Invalid item ID. Please try again.")
    save_menu(menu)  # Save the updated menu

def update_item(menu):
    display_menu(menu)
    item_id = int(input("Enter the item ID of the food to update: "))
    if item_id in menu:
        food, old_price, old_quantity, old_dine_in = menu[item_id]
        new_price = float(input(f"Enter the new price for {food}: "))
        new_quantity = int(input(f"Enter the new quantity for {food}: "))
        print("Select an option for dine-in or take-away:")
        print("1. Dine-in")
        print("2. Take-away")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            new_dine_in = True
        elif choice == '2':
            new_dine_in = False
        else:
            print("Invalid choice. Assuming Take-away.")
            new_dine_in = False

        menu[item_id] = (food, new_price, new_quantity, new_dine_in)
        total_price = new_price * new_quantity
        print(f"{food} price has been updated from ${old_price:.2f} to ${new_price:.2f}.")
        print(f"{food} quantity has been updated from {old_quantity} to {new_quantity}.")
        dine_in_status = "Dine-in" if new_dine_in else "Take-away"
        print(f"{food} dine-in status has been updated to: {dine_in_status}.")
        print(f"Total: ${total_price:.2f}")
    else:
        print("Invalid item ID. Please try again.")
    save_menu(menu)  # Save the updated menu

def main():
    menu = load_menu()

    while True:
        print("Welcome to the Restaurant Menu!")
        print("1. View Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Item")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == '1':
            display_menu(menu)
        elif choice == '2':
            add_item(menu)
        elif choice == '3':
            remove_item(menu)
        elif choice == '4':
            update_item(menu)
        elif choice == '5':
            print("Thank you for using the Restaurant Menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
