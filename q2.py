#Create a program to retrieve, display and update only a range of elements from an array using indexing and slicing in arrays. 
import array as ar
a=ar.array("i",[])
n=int(input("How many elements enters by you:"))

for i in range(n):
    a.append(int(input("Enter element")))


b=a[3:n]
print("retrieve range of element a to b array:",b)

b[2:5] =ar.array("i",[4,6,8])
print("After updating array:",b)


print("display in an array:")
for i in a[2:6]:
    print(i)