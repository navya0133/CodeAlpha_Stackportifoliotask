# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 140,
    "MSFT": 320
}

total_investment = 0
portfolio = {}

print("📈 Welcome to Stock Portfolio Tracker")

# Number of stocks user wants to add
n = int(input("Enter number of stocks you want to add: "))

# Taking user input
for i in range(n):
    stock_name = input("\nEnter stock symbol (AAPL, TSLA, etc): ").upper()

    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        portfolio[stock_name] = {
            "quantity": quantity,
            "investment": investment
        }

    else:
        print("❌ Stock not available in price list.")

# Display portfolio summary
print("\n📊 Portfolio Summary")
print("-" * 30)

for stock, details in portfolio.items():
    print(f"{stock} -> Quantity: {details['quantity']} | Investment: ${details['investment']}")

print("-" * 30)
print(f"💰 Total Investment Value: ${total_investment}")

# Save to text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-" * 30 + "\n")

    for stock, details in portfolio.items():
        file.write(f"{stock} -> Quantity: {details['quantity']} | Investment: ${details['investment']}\n")

    file.write("-" * 30 + "\n")
    file.write(f"Total Investment Value: ${total_investment}")

print("\n✅ Portfolio saved to portfolio.txt")
