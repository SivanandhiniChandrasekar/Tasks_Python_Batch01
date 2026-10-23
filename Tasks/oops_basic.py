
class Product:
    total_products = 0

    def __init__(self, product_id, product_name, price, stock_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock_quantity = stock_quantity

        Product.total_products += 1

    def update_price(self, new_price):
        if new_price > 0:
            self.price = new_price
            print("Price updated successfully!")
        else:
            print("Invalid price!")

    def purchase_product(self, quantity):
        if quantity > 0 and quantity <= self.stock_quantity:
            self.stock_quantity -= quantity
            print("Purchase successful!")
        else:
            print("Insufficient stock")

    def display_details(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Available Stock:", self.stock_quantity)



p1 = Product("P101", "Keyboard", 1200, 10)
p2 = Product("P102", "Mouse", 600, 15)
p3 = Product("P103", "Monitor", 8000, 5)


p1.update_price(1500)
p1.purchase_product(2)
p3.purchase_product(6)

p1.display_details()
p2.display_details()
p3.display_details()

print("Total Products:", Product.total_products)
