#Write a program to accept elements in the form of a tuple and display its minimum, maximum, sum and average.

emp=((2,"sumit",20000),(4,"Amit",25000),(1,"Ankit",30000),(3,"Manmit",35000))



print("Elements in tuple are:",emp)

print()



print("Sorted tuple:",sorted(emp))

print()



print("Reverse sorted tuple:",sorted(emp,reverse=True))

print()



print("Salary wise sorting:",sorted(emp,key=lambda x:x[2]))

# print("Salary wise sorting:",sorted(emp,key=lambda x:x[2],reverse=True))

print()

