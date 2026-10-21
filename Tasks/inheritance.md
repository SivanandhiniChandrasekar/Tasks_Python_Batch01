# E-Commerce Management System — Day 3: Inheritance

## Objective

Extend the existing E-Commerce Management System using inheritance and method overriding.

### Concepts to be used

- Parent class and child class
- Inheritance
- Code reusability
- `super()`
- Method overriding

## Scenario

An online store sells different types of products:

1. Physical products — keyboards, mice, monitors.
2. Digital products — e-books, software, online courses.

Both product types have common details such as product ID, name, and price. However, they have different additional details.

Instead of writing separate classes from scratch, use inheritance to reuse common attributes and methods.

## Task 1: Create a parent class — `Product`

### Attributes

- `product_id`
- `product_name`
- `price`

### Methods

**1. `display_details()`**

Display the product ID, name, and price.

**2. `update_price(new_price)`**

Update the product price.

## Task 2: Create a child class — `PhysicalProduct`

Inherit from `Product`.

### Additional attribute

- `stock_quantity`

### Methods

**1. `purchase_product(quantity)`**

- Check stock availability.
- Reduce stock when sufficient stock is available.
- Display an error message if stock is insufficient.

**2. Override `display_details()`**

Display the common product details along with stock quantity.

Use `super().display_details()` to reuse the parent method.

## Task 3: Create another child class — `DigitalProduct`

Inherit from `Product`.

### Additional attribute

- `file_size_mb`

### Method

Override `display_details()` to display the common product details along with the digital file size.

A digital product does not need a physical stock quantity.

## Example usage

```python
p1 = PhysicalProduct(
    "P101", "Keyboard", 1200, 10
)

p2 = DigitalProduct(
    "D101", "Python E-Book", 499, 25
)

p1.display_details()
p1.purchase_product(2)

p2.display_details()
```

## Expected behaviour

```text
Product ID: P101
Product Name: Keyboard
Price: 1200
Stock Quantity: 10

Purchase successful!

Product ID: D101
Product Name: Python E-Book
Price: 499
File Size: 25 MB
```

## Student implementation requirements

1. Create the `Product` parent class.
2. Create `PhysicalProduct` and `DigitalProduct` child classes.
3. Reuse parent attributes through `super().__init__()`.
4. Override `display_details()` in both child classes.
5. Implement stock management only for physical products.
6. Create at least two objects of each child class.

**Important:** Continue using the encapsulation concepts from Day 2 where appropriate. Validate product prices and ensure physical stock never becomes negative.
