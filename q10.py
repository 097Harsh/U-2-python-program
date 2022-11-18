#Write a program to show variable length argument and its use.
from ast import arg
from unicodedata import name


def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
        print("Sum of argument:",sum)

    
add(10,20,30)


def kargs(**kargs):
    for key,value in kargs.items():
        print(key,value)


det = {
    "name": "Harsh",
    "age" : "20"
}

kargs(**det)