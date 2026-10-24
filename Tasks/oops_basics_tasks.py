'''E-Commerce Management System — Day 1

# Objective

Create a simple E-Commerce Management System using basic Python OOP concepts.

## Concepts to be used

- Class and object
- `__init__()` and `self`
- Instance variables and class variables
- Instance methods
- Object state modification

# Scenario

An online store wants to maintain product details, update product prices, and check product availability.

Create a `Product` class to manage these operations.

Requirements'''
'''
1. Create a `Product` class

The class should contain the following attributes:

- `product_id`
- `product_name`
- `price`
- `stock_quantity`
- `total_products` — class variable to count the products created.

### 2. Implement the following methods

**Function 1: `update_price(new_price)`**

- Update the product price.
- Accept the new price as an argument.
- Display the updated price.

**Function 2: `purchase_product(quantity)`**

- Check whether the requested quantity is available.
- If available, reduce the stock quantity.
- Otherwise, display `"Insufficient stock"`.

**Function 3: `display_details()`**

Display the following details:

- Product ID
- Product name
- Price
- Available stock

## Example usage

```python
p1 = Product("P101", "Keyboard", 1200, 10)
p2 = Product("P102", "Mouse", 600, 15)

p1.update_price(1500)
p1.purchase_product(2)
p1.display_details()

print("Total Products:", Product.total_products)
```

## Expected output

```text
Price updated successfully!
Purchase successful!
Product ID: P101
Product Name: Keyboard
Price: 1500
Available Stock: 8
Total Products: 2
```

## Student tasks

1. Implement the `Product` class.
2. Create at least three product objects.
3. Update the price of one product.
4. Purchase products and check stock modification.
5. Display the details of each product.

**Condition:** Use only the concepts covered on Day 1. Do not use encapsulation, private attributes, getters, setters, or properties yet.'''

class Product:
    total_products = 0
    def __init__(self,product_id,product_name,price,stock_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock_quantity = stock_quantity

        Product.total_products += 1

    def update_price(self,new_price):
        self.price = new_price
        print("Price Updated Successfully !")

    def purchase_product(self,quantity):
        if self.stock_quantity >= quantity:
            self.stock_quantity = self.stock_quantity - quantity
            print("Purchase successfull ! ")
        else:
            print("Insuffficient stock")

    def display_details(self):
        print("Product ID : ", self.product_id)
        print("Product Name : ", self.product_name)
        print("Product Price : ", self.price)
        print("Quantity : ", self.stock_quantity)

p1 = Product("p01","Laptop",75000,15)
p2 = Product("p02","Air Conditioner",30000,20)
p3 = Product("p03","Air Fryer",5000,10)


p3.update_price(5500)

p1.purchase_product(2)
p2.purchase_product(5)
p3.purchase_product(3)

p1.display_details()
p2.display_details()
p3.display_details()

print("Total Products:", Product.total_products)



    


