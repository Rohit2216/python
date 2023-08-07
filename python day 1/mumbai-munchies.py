import json

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def add_snack(name, price, quantity, available=True):
    snacks_data = load_data('snacks_data.json')  # Load existing data
    snack_id = len(snacks_data) + 1  # Assign a unique ID to the snack
    snack = {
        'id': snack_id,
        'name': name,
        'price': price,
        'quantity': quantity,  # New attribute for snack quantity
        'available': available,
        'quantity_sold': 0  # Initialize quantity sold to 0
    }
    snacks_data.append(snack)
    save_data(snacks_data, 'snacks_data.json')

def get_snack_by_id(snack_id):
    snacks_data = load_data('snacks_data.json')
    for snack in snacks_data:
        if snack['id'] == snack_id:
            return snack
    return None

def remove_snack(snack_id):
    snacks_data = load_data('snacks_data.json')
    snacks_data = [snack for snack in snacks_data if snack['id'] != snack_id]
    save_data(snacks_data, 'snacks_data.json')

def update_snack_availability(snack_id, available):
    snacks_data = load_data('snacks_data.json')
    for snack in snacks_data:
        if snack['id'] == snack_id:
            snack['available'] = available
            save_data(snacks_data, 'snacks_data.json')
            break

def sell_snack(snack_id):
    snacks_data = load_data('snacks_data.json')
    snack = get_snack_by_id(snack_id)
    if snack is not None:
        if snack['available']:
            print(f"Available Quantity: {snack['quantity']}")
            try:
                quantity_sold = int(input("Enter the quantity to sell: "))
                if quantity_sold > snack['quantity']:
                    print("Not enough quantity available for sale.")
                else:
                    snack['quantity_sold'] += quantity_sold
                    snack['quantity'] -= quantity_sold  # Decrease snack quantity after selling
                    save_data(snacks_data, 'snacks_data.json')
                    record_sale(snack['id'], snack['name'], snack['price'], quantity_sold)
                    print(f"Sold {quantity_sold} {snack['name']} for ${snack['price']} each.")
                    view_inventory()  # View updated inventory after the sale
                    view_sale_details()  # View updated sale details after the sale
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")
        else:
            print(f"{snack['name']} is not available.")
    else:
        print("Snack not found.")

def record_sale(snack_id, snack_name, price, quantity_sold):
    sale_details = load_data('sale_details.json')
    sale = {
        'snack_id': snack_id,
        'snack_name': snack_name,
        'price': price,
        'quantity_sold': quantity_sold
    }
    sale_details.append(sale)
    save_data(sale_details, 'sale_details.json')

def view_inventory():
    all_snacks = load_data('snacks_data.json')
    for snack in all_snacks:
        availability = "Available" if snack['available'] else "Not Available"
        print(f"{snack['id']}. {snack['name']} - Price: ${snack['price']}, Quantity: {snack['quantity']}, {availability}, Quantity Sold: {snack['quantity_sold']}")

def view_sale_details():
    sale_details = load_data('sale_details.json')
    for sale in sale_details:
        print(f"Snack ID: {sale['snack_id']}, Snack Name: {sale['snack_name']}, Price: ${sale['price']}, Quantity Sold: {sale['quantity_sold']}")

if __name__ == "__main__":
    while True:
        print("1. Add a snack")
        print("2. View inventory")
        print("3. Remove a snack")
        print("4. Update snack availability")
        print("5. Sell a snack")
        print("6. View sale details")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the snack name: ")
            try:
                price = float(input("Enter the price: "))
                quantity = int(input("Enter the quantity: "))  # New input for snack quantity
                add_snack(name, price, quantity)
            except ValueError:
                print("Invalid input. Price and quantity should be numbers.")
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            try:
                snack_id = int(input("Enter the snack ID to remove: "))
                remove_snack(snack_id)
            except ValueError:
                print("Invalid input. Please enter a valid snack ID.")
        elif choice == '4':
            try:
                snack_id = int(input("Enter the snack ID to update availability: "))
                available = input("Enter 'yes' if available, 'no' otherwise: ").lower() == 'yes'
                update_snack_availability(snack_id, available)
            except ValueError:
                print("Invalid input. Please enter a valid snack ID.")
        elif choice == '5':
            try:
                snack_id = int(input("Enter the snack ID to sell: "))
                sell_snack(snack_id)
            except ValueError:
                print("Invalid input. Please enter a valid snack ID.")
        elif choice == '6':
            view_sale_details()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
