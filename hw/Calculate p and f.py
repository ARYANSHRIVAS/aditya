#Write a Python program to calculate profit and loss using the given cost price and selling price

cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    profit = sp - cp
    print("Profit =", profit)

if cp > sp:
    loss = cp - sp
    print("Loss =", loss)

if cp == sp:
    print("No Profit, No Loss")