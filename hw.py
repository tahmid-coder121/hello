buying_price = float(input("Enter buying price: "))
selling_price = float(input("Enter selling price: "))

difference = selling_price - buying_price

if difference > 0:
    print(f"Profit: ${difference:.2f}")
elif difference < 0:
    print(f"Loss: ${abs(difference):.2f}")
else:
    print("No profit, no loss")