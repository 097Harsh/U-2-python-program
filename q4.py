

l = [23,16,9,12,25,86,13]
print("Orginal list:",l)
n = len(l)

for i in range(n):
 
  for j in range(n-1):
  
    if(l[j]>l[j+1]):
     
      l[j],l[j+1] = l[j+1],l[j]

  
print("Sort list:",l)
