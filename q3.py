# Write a program to understand various methods of array class mentioned: append, insert, remove, pop, index, tolist and count.

import array as ar

n=int(input("How many element you wants to enters:"))
a=ar.array("i",range(n))

for i in range(n):
    a[i] = int(input("Element enter:"))

print(a)
print()


apnd = int(input("Enter new element"))
a.append(apnd)
print(a)

print("For insert,")

pos = int(input("Enter position:"))

nval = int(input("Enter new Value:"))

a.insert(pos, nval)

print(a)


rmv = int(input("Remove Element:"))

a.remove(rmv)

print(a)

# pop

a.pop()

print("After pop in the array:",a)

print()



# index

ind = int(input("Enter Element:"))

ind1 = a.index(ind)

print("Index of Element: ",ind1)

print()



# tolist

tlst = a.tolist()

print("List is :",tlst)

print("Array is :",a)



# count

print("Counting an array :",a.count(2))

