#Create a dictionary that will accept cricket players name and scores in a match. Also we are retrieving runs by entering the player’s name.

 dic={}

n=int(input("How many key-value you want to enter:"))



for i in range(n):

      k=input("Enter key(Player name)=")

      v=input("Enter value(Runs)=")

      dict.update({k:v})

print()



print("Players in match:")

for pname in dict.keys():

          print(pname)

print()



name = input("Enter palyer name to get his score:")

print("player runs:", dict[name])