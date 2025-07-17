from string import Template

# Task 1: Input
product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Product Price: "))
categories = input("Enter Categories (comma separated): ").split(",")
stock_available = int(input("Enter Stock Available: "))
stock_sold = int(input("Enter Stock Sold: "))
discount = float(input("Enter Discount Percentage: "))
features = set(input("Enter Product Features (comma separated): ").split(","))
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact: ")
supplier_location = input("Enter Supplier Location: ")
supplier_details = {
    "Name": supplier_name,
    "Contact": supplier_contact,
    "Location": supplier_location
}
stock_details = (stock_available, stock_sold)

print("\n--- Output Using Different Formatting Methods ---\n")

# 1. Comma separated
print("Comma separated:", product_id, product_name, price, categories, stock_details, discount, features, supplier_details, sep=", ")

# 2. Percentage formatting
print("\nPercentage formatting: Product %s costs Rs. %.2f with %.1f%% discount." % (product_name, price, discount))

# 3. f-string
print(f"\nf-string: Product ID: {product_id}, Name: {product_name}, Categories: {categories}")

# 4. .format() method
print("\n.format(): Stock: Available = {}, Sold = {}".format(stock_details[0], stock_details[1]))

# 5. Concatenation
print("\nConcatenation: " + "Supplier - " + supplier_details["Name"] + ", Contact - " + supplier_details["Contact"])

# 6. Template string
template = Template("\nTemplate: '$name' is available for Rs.$price in $location.")
print(template.substitute(name=product_name, price=price, location=supplier_details["Location"]))
