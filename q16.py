#Create a sample list of 7 elements and implement the List methods mentioned: append, insert, copy, extend, count, remove, pop, sort, reverse and clear

from ast import Num


list =[10,20,30,40,50,60,70]

list.append(60)
print("Append=",list)
print()

list.insert(0,5)
print("Inserting num 5 and 0th position=",list)
print()

n=list.copy()
print("Newly creates list n=",n)
print()

list.extend()
print("After extending list=",list)
print()

num = list.count(50)
print("No. of times found in list:",num)
print()

list.remove(50)
print("After removing 50=",list)
print()

n1 = list.pop()
print("popped element is:",n1)
print()

list.sort()
print("After sorting=",list)
print()

list.reverse()
print("After reveresing:",list)
print()

list.clear()
print("After clearing=",list)