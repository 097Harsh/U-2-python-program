#Create a python function to accept python function as a dictionary and display its elements.

def dic(d):
    for key in d:
        print("key:",key,"value:",d[key])


e ={"a":1,"b":2,"c":3}
dic(e)