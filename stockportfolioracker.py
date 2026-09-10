import csv
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}


portfolio = []
total_investment = 0

print("===================================")
print("     STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", "$" + str(price))
while True:

    stock = input("\nEnter stock symbol: ").upper()

    
    if stock in stock_prices:

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            
            price = stock_prices[stock]

          
            investment = price * quantity

           
            total_investment += investment

           
            portfolio.append({
                "stock": stock,
                "quantity": quantity,
                "price": price,
                "investment": investment
            })

            print(
                stock,
                "investment value: $",
                investment
            )

        except ValueError:
            print("Please enter a valid number for quantity.")

    else:
        print("Stock not found. Please choose from the available stocks.")

   
    again = input("Do you want to add another stock? (yes/no): ").lower()

    if again != "yes":
        break
print("\n===================================")
print("          YOUR PORTFOLIO")
print("===================================")

for item in portfolio:
    print(
        item["stock"],
        "| Quantity:", item["quantity"],
        "| Price: $", item["price"],
        "| Investment: $", item["investment"]
    )

print("-----------------------------------")
print("Total Investment: $", total_investment)
with open("portfolio.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Stock",
        "Quantity",
        "Price",
        "Investment"
    ])

    for item in portfolio:
        writer.writerow([
            item["stock"],
            item["quantity"],
            item["price"],
            item["investment"]
        ])

    writer.writerow([])
    writer.writerow([
        "Total Investment",
        total_investment
    ])

print("\nPortfolio saved to portfolio.csv")


