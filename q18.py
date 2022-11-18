#Write a program to accept elements in the form of a tuple and display its minimum, maximum, sum and average.
no = int(input("How many elements you want to added:"))
tuple =()

for i in range(no):
    tuple = tuple + (int(input("Enter element:")))

print()
print("Maximum=",max(tuple))

print()
print("Minimum=",min(tuple))

print()
print("Sum is=",sum(tuple))

print()
avg = sum(tuple)/len(tuple)
print("Average is=",avg)