# Create a decorator function to increase the value of a function by 3.

def decor(func):
    def inner(*args):
        val = func(*args)
        return val+3

    return inner

def num(x):
    return x

n=int(input("Enter number:"))
print(num(n))
