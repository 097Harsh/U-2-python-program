#Write a program to create nested list and display its elements
list =[1,2,3,[4,5,6]]
print("main list:",list)

n=list[3]
print("Neasted list:",n)

print("element in nested list are:")

for i  in n:
    print(i)