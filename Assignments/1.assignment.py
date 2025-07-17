from string import Template

# Government Header
print("\n========================================")
print("  Government of India - Citizen Service Portal")
print("========================================\n")

# Input Citizen Details
citizen_id = int(input("Enter Citizen ID: "))
name = input("Enter Full Name: ")
age = int(input("Enter Age: "))
aadhar = input("Enter Aadhaar Number: ")
schemes = input("Enter Applied Schemes (comma separated): ").split(",")
income = float(input("Enter Annual Income (in ₹): "))
eligibility_score = float(input("Enter Eligibility Score (0-100): "))
documents = set(input("Enter Documents Submitted (comma separated): ").split(","))
address = input("Enter Residential Address: ")
district = input("Enter District: ")
contact = input("Enter Mobile Number: ")

# Package address info
contact_info = {
    "Address": address,
    "District": district,
    "Contact": contact
}
status = (income, eligibility_score)

# Output using formatting
print("\n--- Citizen Registration Summary ---\n")

# 1. Comma separated
print("Comma separated:", citizen_id, name, age, aadhar, schemes, status, documents, contact_info, sep=", ")

# 2. Percentage formatting
print("\nPercentage formatting: Citizen %s (Age %d) has %.1f%% eligibility score for schemes." % (name, age, eligibility_score))

# 3. f-string
print(f"\nf-string: Aadhaar: {aadhar}, District: {district}, Schemes Applied: {schemes}")

# 4. .format()
print("\n.format(): Annual Income: ₹{:.2f}, Eligibility Score: {}%".format(status[0], status[1]))

# 5. Concatenation
print("\nConcatenation: Contact - " + contact + " | Name - " + name)

# 6. Template String
template = Template("\nTemplate: '$name' (ID: $id) has registered from $district with ₹$income income.")
print(template.substitute(name=name, id=citizen_id, district=district, income=income))
