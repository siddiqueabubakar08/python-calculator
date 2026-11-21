
# Employee Salary Calculator with User Input

print("EMPLOYEE SALARY CALCULATOR")
print("--------------------------")

basic_salary = float(input("Enter Basic Salary: "))
hra = float(input("Enter HRA: "))
allowance = float(input("Enter Allowance: "))
pf = float(input("Enter PF Deduction: "))

gross_salary = basic_salary + hra + allowance
net_salary = gross_salary - pf

print("\n----- SALARY DETAILS -----")
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("Allowance:", allowance)
print("Gross Salary:", gross_salary)
print("PF Deduction:", pf)
print("Net Salary:", net_salary)
