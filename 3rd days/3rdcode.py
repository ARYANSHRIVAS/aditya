
print("Press 1 for Addition")
print("Press 2 for Subtraction")

ch = int(input("Enter your choice: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if ch == 1:
    c = a + b
    print("Sum =", c)

elif ch == 2:
    c = a - b
    print("Subtraction =", c)

else:
    print("Invalid choice")
