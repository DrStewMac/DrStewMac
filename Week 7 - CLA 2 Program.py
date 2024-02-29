class Drink:
    def __init__(self, name, price, ingredients, cup_size):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.cup_size = cup_size

class Inventory:
    def __init__(self):
        self.stock = {}

    def add_stock(self, ingredient, quantity):
        if ingredient in self.stock:
            self.stock[ingredient] += quantity
        else:
            self.stock[ingredient] = quantity

    def deduct_stock(self, ingredients):
        for ingredient, quantity in ingredients.items():
            self.stock[ingredient] -= quantity

class Customer:
    def __init__(self, name, membership_number=None):
        self.name = name
        self.membership_number = membership_number
        self.orders = []
        self.num_orders = 0

class CoffeeShop:
    def __init__(self):
        self.menu = {}
        self.inventory = Inventory()
        self.sales = 0
        self.customers = {}

    def add_drink_to_menu(self, drink):
        self.menu[drink.name] = drink

    def login(self):
        customer_name = input("Enter your name: ")
        if customer_name in self.customers:
            return self.customers[customer_name]
        else:
            new_customer = input("New customer? (yes/no): ").lower()
            if new_customer == "yes":
                join_club = input("Would you like to join our coffee club? (yes/no): ").lower()
                if join_club == "yes":
                    membership_number = input("Enter your desired membership number: ")
                    customer = Customer(customer_name, membership_number)
                else:
                    customer = Customer(customer_name)
                self.customers[customer_name] = customer
                return customer
            else:
                print("Customer not found.")
                return None

    def order_drink(self, customer, drink_name, cup_size):
        if drink_name in self.menu:
            drink = self.menu[drink_name]
            if self.check_inventory(drink.ingredients):
                payment_method = input("Enter payment method (cash/card): ").lower()
                if payment_method == "cash":
                    self.process_cash_payment(customer, drink.price)
                elif payment_method == "card":
                    self.process_card_payment(customer, drink.price)
                else:
                    print("Invalid payment method.")
                    return
                self.inventory.deduct_stock(drink.ingredients)
                customer.orders.append((drink_name, cup_size))
                customer.num_orders += 1
                if customer.num_orders == 5:
                    print("Congratulations! You've earned a free drink of your choice.")
                    self.claim_free_drink(customer)
                print(f"Enjoy your {cup_size} {drink_name}!")
            else:
                print("Sorry, not enough ingredients to make the drink.")
        else:
            print("Sorry, that drink is not on the menu.")

    def check_inventory(self, ingredients):
        for ingredient, quantity in ingredients.items():
            if ingredient not in self.inventory.stock or self.inventory.stock[ingredient] < quantity:
                return False
        return True

    def process_cash_payment(self, customer, amount):
        # Logic for processing cash payment
        self.sales += amount
        print(f"Payment of ${amount} received in cash from {customer.name}.")

    def process_card_payment(self, customer, amount):
        # Logic for processing card payment
        self.sales += amount
        print(f"Payment of ${amount} received via card from {customer.name}.")

    def claim_free_drink(self, customer):
        print("Here are the available drinks for your free choice:")
        for drink_name in self.menu:
            print(drink_name)
        chosen_drink = input("Enter the name of the drink you'd like for free: ")
        if chosen_drink in self.menu:
            print(f"Congratulations, {customer.name}! You've claimed a free {chosen_drink}.")
            self.inventory.deduct_stock(self.menu[chosen_drink].ingredients)
            customer.orders.append((chosen_drink, "Small"))
        else:
            print("Invalid drink choice.")

    def calculate_final_cost(self, customer):
        total_cost = 0
        for order in customer.orders:
            drink_name, _ = order
            total_cost += self.menu[drink_name].price
        sales_tax = total_cost * 0.0325
        total_cost += sales_tax
        return total_cost

    def generate_report(self):
        print("Sales Report:")
        print(f"Total Sales: ${self.sales}")
        print("Inventory:")
        for ingredient, quantity in self.inventory.stock.items():
            print(f"{ingredient}: {quantity}")
        print("Customer Orders:")
        for customer_name, customer in self.customers.items():
            print(f"{customer_name}:")
            for order in customer.orders:
                print(f" - {order[1]} {order[0]}")
            print(f"Total Cost: ${self.calculate_final_cost(customer)}")

# Instantiate a coffee shop
my_coffee_shop = CoffeeShop()

# Add drinks to the menu with different cup sizes
espresso_small = Drink("Espresso", 2.5, {"coffee": 1}, "Small")
espresso_medium = Drink("Espresso", 3.0, {"coffee": 1}, "Medium")
espresso_large = Drink("Espresso", 3.5, {"coffee": 1}, "Large")
latte_small = Drink("Latte", 3.5, {"coffee": 1, "milk": 1}, "Small")
latte_medium = Drink("Latte", 4.0, {"coffee": 1, "milk": 1}, "Medium")
latte_large = Drink("Latte", 4.5, {"coffee": 1, "milk": 1}, "Large")
cappuccino_small = Drink("Cappuccino", 3.0, {"coffee": 1, "milk": 1, "foam": 1}, "Small")
cappuccino_medium = Drink("Cappuccino", 3.5, {"coffee": 1, "milk": 1, "foam": 1}, "Medium")
cappuccino_large = Drink("Cappuccino", 4.0, {"coffee": 1, "milk": 1, "foam": 1}, "Large")

my_coffee_shop.add_drink_to_menu(espresso_small)
my_coffee_shop.add_drink_to_menu(espresso_medium)
my_coffee_shop.add_drink_to_menu(espresso_large)
my_coffee_shop.add_drink_to_menu(latte_small)
my_coffee_shop.add_drink_to_menu(latte_medium)
my_coffee_shop.add_drink_to_menu(latte_large)
my_coffee_shop.add_drink_to_menu(cappuccino_small)
my_coffee_shop.add_drink_to_menu(cappuccino_medium)
my_coffee_shop.add_drink_to_menu(cappuccino_large)

# Add sweeteners, creamers, and coffee flavors to inventory
my_coffee_shop.inventory.add_stock("sugar", 20)
my_coffee_shop.inventory.add_stock("cream", 20)
my_coffee_shop.inventory.add_stock("vanilla", 20)
my_coffee_shop.inventory.add_stock("caramel", 20)

# Add initial stock of coffee
my_coffee_shop.inventory.add_stock("coffee", 60)  # Assuming all sizes use the same coffee

# Example usage:
customer = my_coffee_shop.login()
if customer:
    my_coffee_shop.order_drink(customer, "Espresso", "Small")
    my_coffee_shop.order_drink(customer, "Latte", "Medium")
    my_coffee_shop.order_drink(customer, "Cappuccino", "Large")
    my_coffee_shop.generate_report()
