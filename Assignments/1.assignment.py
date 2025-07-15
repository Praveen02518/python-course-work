#Product Information System Using Different Data Types and Formatting Methods

#Welcome to the e-commerce website
print(""*50, "\n Welcome to the e-commerce website \n" + ""*50)
# Product Details Input
product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
product_quantity = int(input("Enter product quantity: "))
in_stock = input("Is the product in stock? (yes/no): ").strip().lower() == "yes"
categories = input("Enter product categories (comma-separated): ").split(',')

# Data Types Example
product = {
    "name": product_name,
    "price": product_price,
    "quantity": product_quantity,
    "in_stock": in_stock,
    "categories": [c.strip() for c in categories]
}

# Output 1: Comma-Separated Format
print("\n--- Comma-Separated Output ---")
print("Product Name,", "Price,", "Quantity,", "In Stock,", "Categories")
print(product["name"], ",", product["price"], ",", product["quantity"], ",", product["in_stock"], ",", product["categories"])

# Output 2: Percentage Formatting
print("\n--- Percentage Formatting Output ---")
print("Product Price: %.2f" % product["price"])
print("Total Price (Qty x Price): %.2f" % (product["quantity"] * product["price"]))

# Output 3: f-string Formatting
print("\n--- f-string Output ---")
print(f"Product '{product['name']}' belongs to categories: {', '.join(product['categories'])}")
print(f"In Stock: {product['in_stock']} | Quantity: {product['quantity']} | Total Value: ₹{product['quantity'] * product['price']:.2f}")

# Output 4: .format() method
print("\n--- .format() Method Output ---")
output = "Product: {}\nPrice per Unit: ₹{:.2f}\nQuantity: {}\nStock Available: {}\nCategories: {}"
print(output.format(
    product["name"],
    product["price"],
    product["quantity"],
    product["in_stock"],
    ', '.join(product["categories"])
))
