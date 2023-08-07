# Step 2: Implementing Menu Mastery

# Initialize the menu dictionary with some dishes.
menu = {
    1: {'name': 'Margherita Pizza', 'price': 12.99, 'availability': True},
    2: {'name': 'Pasta Carbonara', 'price': 10.99, 'availability': True},
    # Add more dishes here
}

# Function to display the entire menu with all its details.
def display_menu(menu):
    for dish_id, dish_info in menu.items():
        print("-------------------------------------")
        print(f"Dish ID: {dish_id}")
        print(f"Name: {dish_info['name']}")
        print(f"Price: ${dish_info['price']:.2f}")
        availability_status = "Yes" if dish_info['availability'] else "No"
        print(f"Availability: {availability_status}")
    print("-------------------------------------")

# Function to add a new dish to the menu.
def add_dish_to_menu(menu, name, price, availability):
    next_dish_id = max(menu.keys(), default=0) + 1
    new_dish = {'name': name, 'price': price, 'availability': availability}
    menu[next_dish_id] = new_dish

# Function to remove a dish from the menu.
def remove_dish_from_menu(menu, dish_id):
    menu.pop(dish_id, None)

# Function to update the availability of a dish.
def update_dish_availability(menu, dish_id, availability):
    if dish_id in menu:
        menu[dish_id]['availability'] = availability

# Function to get user input for adding a new dish.
def get_new_dish_input():
    name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    availability = input("Is the dish available (yes/no): ").lower() == 'yes'
    return name, price, availability

# Main program
while True:
    print("\n---- Zesty Zomato Menu Management ----")
    print("1. Display Menu")
    print("2. Add a New Dish")
    print("3. Remove a Dish")
    print("4. Update Dish Availability")
    print("5. Exit")

    choice = int(input("Enter your choice (1/2/3/4/5): "))

    if choice == 1:
        display_menu(menu)
    elif choice == 2:
        name, price, availability = get_new_dish_input()
        add_dish_to_menu(menu, name, price, availability)
        print("Dish added successfully!")
    elif choice == 3:
        dish_id = int(input("Enter the Dish ID to remove: "))
        remove_dish_from_menu(menu, dish_id)
        print("Dish removed successfully!")
    elif choice == 4:
        dish_id = int(input("Enter the Dish ID to update availability: "))
        availability = input("Is the dish available (yes/no): ").lower() == 'yes'
        update_dish_availability(menu, dish_id, availability)
        print("Availability updated successfully!")
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
