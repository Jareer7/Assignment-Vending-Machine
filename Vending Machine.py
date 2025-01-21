class VendingMachine:
    def __init__(self):
        # Initialize products with names, prices, stock levels, and categories
        self.products = {
            '1': {'name': 'Biscuits🍪', 'price': 1.50, 'stock': 6, 'category': 'snacks'},
            '2': {'name': 'Chips🥔', 'price': 1.25, 'stock': 10, 'category': 'snacks'},
            '3': {'name': 'Chocolate🍫', 'price': 1.75, 'stock': 4, 'category': 'snacks'},
            '4': {'name': 'Candy🍭', 'price': 0.75, 'stock': 8, 'category': 'snacks'},
            '5': {'name': 'Coke🥤', 'price': 1.50, 'stock': 6, 'category': 'cold drinks'},
            '6': {'name': 'Water💧', 'price': 1.00, 'stock': 5, 'category': 'cold drinks'},
            '7': {'name': 'Lemonade🍋', 'price': 1.25, 'stock': 4, 'category': 'cold drinks'},
            '8': {'name': 'Hot Chocolate☕', 'price': 2.50, 'stock': 4, 'category': 'hot drinks'},
            '9': {'name': 'Coffee☕', 'price': 2.00, 'stock': 3, 'category': 'hot drinks'},
            '10': {'name': 'Tea🍵', 'price': 1.50, 'stock': 5, 'category': 'hot drinks'},
            '11': {'name': 'Orange Juice🍹', 'price': 2.50, 'stock': 4, 'category': 'fresh juices'},
            '12': {'name': 'Apple Juice🧃', 'price': 2.50, 'stock': 4, 'category': 'fresh juices'},
        }
        
        # Suggestions for each product
        self.suggestions = {
            '1': ['2', '3'],  # Biscuits suggests Chips and Chocolate
            '2': ['1', '4'],  # Chips suggests Biscuits and Candy
            '3': ['1', '2'],  # Chocolate suggests Biscuits and Chips
            '4': ['2'],       # Candy suggests Chips
            '5': ['6', '11'], # Coke suggests Water and Lemonade
            '6': ['5'],       # Water suggests Coke
            '7': ['8'],       # Coffee suggests Tea
            '8': ['7'],       # Tea suggests Coffee
            '9': ['10'],      # Orange Juice suggests Apple Juice
            '10': ['9'],      # Apple Juice suggests Orange Juice
            '11': ['5'],      # Lemonade suggests Coke
            '12': ['7', '8']  # Hot Chocolate suggests Coffee and Tea
        }

    def display_menu(self):
        # Show available products and their details categorized
        print("Welcome to our Vending Machine!")
        categories = {}
        for code, product in self.products.items():
            category = product['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(f"{code}: {product['name']} - £{product['price']} (Stock: {product['stock']})")
        
        for category, items in categories.items():
            print(f"\n{category.capitalize()}:\n" + "\n".join(items))

    def get_user_input(self):
        # Prompt user for product code
        while True:
            code = input("Please enter the product code: ").strip()
            if code in self.products:
                return code
            else:
                print("Invalid product code. Please try again.")

    def choose_payment_method(self):
        # Allow user to choose a payment method
        while True:
            print("Choose a payment method:")
            print("1: Cash")
            print("2: Card")
            print("3: Mobile Payment")
            choice = input("Enter the number of your choice: ")
            if choice in ['1', '2', '3']:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def process_payment(self, product):
        # Handle payment and return change
        payment_method = self.choose_payment_method()
        if payment_method == '1':  # Cash
            while True:
                try:
                    money_inserted = float(input(f"Insert money for {product['name']} (£{product['price']}): £"))
                    if money_inserted < product['price']:
                        print("Insufficient amount. Please insert more money.")
                    else:
                        change = money_inserted - product['price']
                        return change
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
        elif payment_method in ['2', '3']:  # Card or Mobile Payment
            print(f"Processing {['Card', 'Mobile Payment'][int(payment_method) - 2]} payment...")
            return 0  # No change for card or mobile payment

    def vend_product(self, code):
        # Retrieve the product by code
        product = self.products[code]
         # Check stock availability
        if product['stock'] > 0:
            change = self.process_payment(product) # Process payment
            product['stock'] -= 1 # Decrease stock
            print(f"Dispensing {product['name']}. Change returned: £{change:.2f}")
            self.suggest_products(code) # Suggest related products
        else:
            print("Sorry, this product is out of stock.")

    def suggest_products(self, code):
         # Get and display product suggestions
        suggestions = self.suggestions.get(code, [])
        if suggestions:
            print("You might also like:")
            for suggestion in suggestions:
                suggested_product = self.products[suggestion]
                print(f"- {suggested_product['name']} (£{suggested_product['price']})")

    def run(self):
        self.display_menu()  # Show the menu
        while True:
            code = self.get_user_input() # Get user input
            self.vend_product(code) # Vend the selected product
            if input("Do you want to purchase another item? (yes/no): ").strip().lower() != 'yes':
                print("Thank you for using our vending machine!") # Exit message
                break


# Create an instance of the vending machine and run it
vending_machine = VendingMachine()
vending_machine.run()