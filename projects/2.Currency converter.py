import requests

conversion_history = []

def convert_currency(from_currency, to_currency, amount):
    try:
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
        response = requests.get(url)
        data = response.json()

        if to_currency in data["rates"]:
            result = data["rates"][to_currency]
            print(f"✅ {amount} {from_currency} = {result:.2f} {to_currency}")
            history = f"{amount} {from_currency} = {result:.2f} {to_currency}"
            conversion_history.append(history)
        else:
            print("❌ Invalid currency code.")
    except Exception as e:
        print("❌ Error:", str(e))

def view_history():
    if not conversion_history:
        print("📭 No conversion history yet.")
    else:
        print("📜 Conversion History:")
        for record in conversion_history:
            print("•", record)

def save_history_to_file():
    try:
        with open("conversion_history.txt", "w") as file:
            for record in conversion_history:
                file.write(record + "\n")
        print("💾 History saved to 'conversion_history.txt'")
    except Exception as e:
        print("❌ Failed to save history:", str(e))

def main():
    while True:
        print("\n====== Currency Converter Menu ======")
        print("1. Convert Currency")
        print("2. View Conversion History")
        print("3. Save History to File")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            from_currency = input("From Currency (e.g., USD): ").upper()
            to_currency = input("To Currency (e.g., INR): ").upper()
            try:
                amount = float(input("Amount to convert: "))
                convert_currency(from_currency, to_currency, amount)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "2":
            view_history()
        elif choice == "3":
            save_history_to_file()
        elif choice == "4":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
