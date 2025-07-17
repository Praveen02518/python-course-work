from string import Template

# Government Header
print("\n================================================")
print("  Government of India - Citizen Service Portal")
print("================================================\n")

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


# ---------- Conditional Logic ---------- #

print("\n--- Eligibility Evaluation ---\n")

# 1. Eligibility criteria
if income <= 200000 and eligibility_score >= 60:
    print("✅ Eligible for Government Benefits.")
else:
    print("❌ Not eligible due to income or low score.")

# 2. Senior citizen check
if age >= 60:
    print("🧓 Senior Citizen: Eligible for elderly schemes.")

# 3. Document check
required_docs = {"Aadhaar", "Income Certificate", "Address Proof"}
if required_docs.issubset(documents):
    print("📄 All required documents submitted.")
else:
    missing = required_docs - documents
    print(f"⚠️ Missing documents: {', '.join(missing)}")

# 4. Scheme-specific message
if "HealthCare Yojana" in schemes:
    print("🏥 HealthCare Yojana applied. Medical records will be verified.")
if "Student Scholarship" in schemes and age <= 25:
    print("🎓 Student Scholarship: Application under review.")
elif "Student Scholarship" in schemes and age > 25:
    print("🚫 Not eligible for Student Scholarship due to age.")

# 5. Address check
if "Rural" in address.title():
    print("🌾 Rural Resident: Priority benefits may apply.")
