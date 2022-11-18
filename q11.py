#Write a lambda/Anonymous function to find bigger number in two given numbers.

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

max = lambda num1,num2:num1 if(num1>num2) else num2
print("Max number is:",max(num1,num2))