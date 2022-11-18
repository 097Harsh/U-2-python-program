#Write a program to create a dictionary from the user and display the elements.

dict={}

n=int(input("How many key-value pair you want:"))



for i in range(n):

      k=input("Enter key=")

      v=input("Enter value=")

      dict.update({k:v})

      

print("Elements in dictionary are:")

print(dict) 

