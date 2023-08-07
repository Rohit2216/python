def display_menu(menu):
    print("------ Menu ------")
    for item_id, (food, price) in menu.items():
        print(f"{item_id}. {food} - ${price:.2f}")
    print("------------------")

def add_item(menu):
    item_id = len(menu) + 1
    food = input("Enter the name of the new food: ")
    price = float(input("Enter the price of the new food: "))
    menu[item_id] = (food, price)
    print(f"{food} has been added to the menu.")

def remove_item(menu):
    display_menu(menu)
    item_id = int(input("Enter the item ID of the food to remove: "))
    if item_id in menu:
        food, _ = menu.pop(item_id)
        print(f"{food} has been removed from the menu.")
    else:
        print("Invalid item ID. Please try again.")

def update_item(menu):
    display_menu(menu)
    item_id = int(input("Enter the item ID of the food to update: "))
    if item_id in menu:
        food, old_price = menu[item_id]
        new_price = float(input(f"Enter the new price for {food}: "))
        menu[item_id] = (food, new_price)
        print(f"{food} price has been updated from ${old_price:.2f} to ${new_price:.2f}.")
    else:
        print("Invalid item ID. Please try again.")

def main():
    menu = {}

    while True:
        print("Welcome to the Restaurant Menu!")
        print("1. View Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Item")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            if menu:
                display_menu(menu)
            else:
                print("The menu is empty.")
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
