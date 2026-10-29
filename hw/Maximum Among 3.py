#Write a Python program to find the maximum among 3 numbers using multiple `if` statements
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Maximum number is:", a)

if b > a and b > c:
    print("Maximum number is:", b)

if c > a and c > b:
    print("Maximum number is:", c)