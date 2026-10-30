n = int(input("Enter any number: "))
found = 0 
for i in range(2, n):
    if (n % i == 0):
        found = 1 
        break
if (found == 1) :
    print("Not a prime number")
else:
    print("Prime number")
