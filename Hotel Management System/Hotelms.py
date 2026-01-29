from datetime import datetime

class HotelManagementSystem:
    def __init__(self):
        self.customer_data = {}
        self.room_types = {
            "Economy": 80,
            "Standard": 150,
            "Luxury": 250,
            "Presidential": 500
        }
        self.restaurant_menu = {
            "Veg Sandwich": 30,
            "Grilled Chicken": 50,
            "Caesar Salad": 35,
            "Seafood Platter": 200,
            "Fresh Juice": 20
        }
        self.laundry_rate_per_item = 30
        self.game_rate_per_hour = 75

    def enter_customer_data(self):
        print("\nEnter Customer Details:")
        self.customer_data = {
            'name': input("Full Name: "),
            'phone': input("Contact Number: "),
            'email': input("Email Address: "),
            'check_in': input("Check-in Date (DD-MM-YYYY): "),
            'check_out': input("Check-out Date (DD-MM-YYYY): ")
        }
        print("Customer details recorded successfully!\n")

    def calculate_nights(self):
        try:
            check_in = datetime.strptime(self.customer_data['check_in'], "%d-%m-%Y")
            check_out = datetime.strptime(self.customer_data['check_out'], "%d-%m-%Y")
            nights = (check_out - check_in).days
            if nights <= 0:
                raise ValueError("Check-out date must be after check-in date.")
            return nights
        except (ValueError, KeyError) as e:
            print(f"Error: {e}\nPlease re-enter valid dates.")
            return None

    def calculate_room_rent(self):
        print("\nAvailable Room Types:")
        for room, price in self.room_types.items():
            print(f"{room}: $ {price} per night")

        room_type = input("\nChoose a room type: ")
        if room_type in self.room_types:
            nights = self.calculate_nights()
            if nights:
                rent = self.room_types[room_type] * nights
                self.customer_data.update({'room_type': room_type, 'room_rent': rent})
                print(f"Room rent for {nights} night(s) in {room_type}: $ {rent}\n")
        else:
            print("Invalid room type. Please try again.\n")

    def calculate_restaurant_bill(self):
        print("\nRestaurant Menu:")
        for item, price in self.restaurant_menu.items():
            print(f"{item}: $ {price}")

        total = 0
        while True:
            choice = input("\nEnter the dish name to order (or type 'done' to finish): ").strip()
            if choice.lower() == 'done':
                break
            elif choice in self.restaurant_menu:
                total += self.restaurant_menu[choice]
                print(f"Added {choice} for $ {self.restaurant_menu[choice]}.")
            else:
                print("Invalid choice. Please select a valid dish.")

        self.customer_data['restaurant_bill'] = total
        print(f"\nTotal Restaurant Bill: $ {total}\n")

    def calculate_laundry_bill(self):
        try:
            items = int(input("\nEnter the number of laundry items: "))
            laundry_bill = items * self.laundry_rate_per_item
            self.customer_data['laundry_bill'] = laundry_bill
            print(f"Laundry Bill: $ {laundry_bill}\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

    def calculate_games_bill(self):
        try:
            hours = int(input("\nEnter the number of hours spent playing games: "))
            games_bill = hours * self.game_rate_per_hour
            self.customer_data['games_bill'] = games_bill
            print(f"Games Bill: $ {games_bill}\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

    def calculate_total_cost(self):
        room_rent = self.customer_data.get('room_rent', 0)
        restaurant_bill = self.customer_data.get('restaurant_bill', 0)
        laundry_bill = self.customer_data.get('laundry_bill', 0)
        games_bill = self.customer_data.get('games_bill', 0)

        service_charge = 0.1 * (room_rent + restaurant_bill)
        total_cost = room_rent + restaurant_bill + laundry_bill + games_bill + service_charge
        
        self.customer_data['total_cost'] = total_cost

        print("\n------- Final Bill -------")
        for key, value in self.customer_data.items():
            if key != 'total_cost':
                print(f"{key.replace('_', ' ').title()}: {value}")
        print(f"Service Charge: $ {service_charge:.2f}")
        print(f"Total Cost: $ {total_cost:.2f}")
        print("--------------------------\n")

    def main(self):
        options = {
            '1': self.enter_customer_data,
            '2': self.calculate_room_rent,
            '3': self.calculate_restaurant_bill,
            '4': self.calculate_laundry_bill,
            '5': self.calculate_games_bill,
            '6': self.calculate_total_cost
        }

        while True:
            print("\n**** Hotel Management System ****")
            print("1. Enter Customer Details")
            print("2. Calculate Room Rent")
            print("3. Calculate Restaurant Bill")
            print("4. Calculate Laundry Bill")
            print("5. Calculate Games Bill")
            print("6. Show Total Bill")
            print("7. Exit")

            choice = input("\nSelect an option: ")
            if choice == '7':
                print("\nThank you for using the Hotel Management System. Goodbye!\n")
                break
            elif choice in options:
                options[choice]()
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    HotelManagementSystem().main()
