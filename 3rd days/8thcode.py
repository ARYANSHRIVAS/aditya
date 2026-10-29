n = int(input("Enter a number: "))
temp = n
sum = 0
digits = len(str(n))

while temp > 0:
    rem = temp % 10
    sum = sum + rem ** digits
    temp = temp // 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
