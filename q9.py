#Write a program to demonstrate the use of Positional argument, keyword argument and default arguments
from fnmatch import fnmatch


def posargs(str1, str2):
    print(str1+""+str2)

def keyargs(name,msg="hello world"):
    print(name+""+msg)

def defaultargs(name,price):
    print("name:",name,"price=",price)


fname ="Harsh"
lname = "shah"
posargs(fname,lname)

keyargs("harsh")


defaultargs("harsh",10000)
defaultargs(price=10000,name="Harsh")