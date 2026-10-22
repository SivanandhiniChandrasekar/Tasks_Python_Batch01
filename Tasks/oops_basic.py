class Product:
    total_products = 0

    def __init__(self, product_id, product_name, price, stock_quantity=10, total_products=0):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock_quantity = stock_quantity
        Product.total_products += 1

    def update_price(self, product_name, updated_price):
        if self.product_name == product_name:
            if updated_price > 0:
                self.price = updated_price
                print(f"Price updated successfully! {product_name} price is {self.price}")
            else:
                print("Invalid price")
        else:
            
            if isinstance(product_name, (int, float)) and product_name > 0:
                self.price = product_name
                print("Price updated successfully!")

    def purchase_product(self, quantity=1):
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            print(f"Purchase successful! {quantity} qty purchased.")
        else:
            print("Insufficient stock")
            print(f"{self.product_name} is out of stock")

    def display_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"Available Stock: {self.stock_quantity}")

 ## Student tasks

#  Create at least three product objects
p1 = Product("P101", "Keyboard", 1200, 10)
p2 = Product("P102", "Mouse", 600, 15)
p3 = Product("P103", "Monitor", 10000, 5)

#  Update the price of one product
p1.update_price("Keyboard", 1500)

#  Purchase products and check stock modification
p1.purchase_product(2)
p2.purchase_product(1)

#  Display the details of each product
print("\n--- Final Details ---")
p1.display_details()
print()
p2.display_details()
print()
p3.display_details()
print()
print(f"Total Products: {Product.total_products}")
