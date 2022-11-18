##Create a program name “employee.py” and implement 
#the functions DA, HRA, PF, and ITAX. Create another 
#program that uses the function of employee module and 
#calculates gross and net salaries of an employee.

salary = int(input("Enter your salary:"))
print("Your salary before taxes:",salary)

def myfunc():
    HRA = 0.45 * salary
    DA = 0.09 * salary
    tax = 0.10 * salary
    Netpayment = salary + HRA - DA - tax
    print("TOtal gross salary:",Netpayment)

myfunc()