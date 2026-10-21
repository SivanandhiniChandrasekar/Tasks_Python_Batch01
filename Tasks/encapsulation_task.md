# E-Commerce Management System — Day 2

## Objective

Modify the Day 1 E-Commerce Management System using encapsulation.

Reuse the same `Product` class and implement controlled access to the product price and stock.

### Concepts to be used

- Public and private attributes
- Encapsulation
- Getters and setters
- `@property` and `@setter`
- Basic input validation

## Scenario

The store administrator notices that product prices and stock quantities can be modified incorrectly.

For example, someone might set the price to `-500` or reduce the stock below zero.

Modify the `Product` class to prevent these invalid updates.

## Requirements

### 1. Create a `Product` class

The class should contain:

- `product_id` — public attribute
- `product_name` — public attribute
- `__price` — private attribute
- `__stock_quantity` — private attribute
- `total_products` — class variable

### 2. Implement the following methods and properties

**Function 1: `price` property**

- Create a getter to display the product price.
- Create a setter to update the price.
- Reject prices less than or equal to zero.

**Function 2: `purchase_product(quantity)`**

- Check whether the requested quantity is positive.
- Check whether sufficient stock is available.
- Reduce the stock only when the purchase is valid.
- Reject invalid quantities and insufficient stock.

**Function 3: `stock_quantity` property**

- Create a getter to display the available stock.
- Create a setter to update stock.
- Do not allow negative stock quantities.

## Example usage

```python
p1 = Product("P101", "Keyboard", 1200, 10)

print("Price:", p1.price)
print("Stock:", p1.stock_quantity)

p1.price = 1500
p1.purchase_product(2)

print("Updated Price:", p1.price)
print("Remaining Stock:", p1.stock_quantity)

p1.price = -500
```

## Expected behaviour

```text
Price: 1200
Stock: 10
Purchase successful!
Updated Price: 1500
Remaining Stock: 8
ValueError: Price must be greater than zero
```

The exact error handling and output format may differ depending on your implementation.

## Student tasks

1. Modify the Day 1 implementation.
2. Make price and stock private.
3. Implement getters and setters using properties.
4. Validate the price before updating it.
5. Validate the quantity before purchasing.
6. Test valid and invalid inputs.

**Condition:** Do not change the business scenario. The objective is to understand how encapsulation improves the same implementation from Day 1.
