#Write a Python program to calculate total salary and net salary, where the variables are basic salary, bonus, HRA, and DA (DA is 7.8% of basic salary).

basic = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus: "))
hra = float(input("Enter HRA: "))

da = basic * 7.8 / 100

total_salary = basic + bonus + hra + da
net_salary = total_salary

print("DA =", da)
print("Total Salary =", total_salary)
print("Net Salary =", net_salary)