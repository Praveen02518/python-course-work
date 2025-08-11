from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Currency list (short codes and names for dropdowns)
CURRENCY_CODES = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "INR": "Indian Rupee",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "ZAR": "South African Rand"
}

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        from_currency = request.form.get("from_currency")
        to_currency = request.form.get("to_currency")
        amount = request.form.get("amount")

        try:
            amount = float(amount)

            # Call API for conversion
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(url)
            data = response.json()

            if "rates" in data:
                rate = data["rates"].get(to_currency)
                if rate:
                    converted = round(amount * rate, 2)
                    result = f"{amount} {from_currency} = {converted} {to_currency}"
                else:
                    error = "Invalid target currency selected."
            else:
                error = "Failed to fetch rates. Try again later."

        except ValueError:
            error = "Please enter a valid number for amount."

    return render_template("index.html", currencies=CURRENCY_CODES, result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
