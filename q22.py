#Write a program to convert the elements of two lists into key-value pairs of a dictionary.
list1 = [1, 2, 3, 4]

list2 = ["a", "b", "c", "d"]



#zip is a function combine two tuples or list

d=zip(list1,list2)  

dict1=dict(d)



print("Dictionary=",dict1)