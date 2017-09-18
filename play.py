def  nestedsum(t):
 total = 0
 for i in t:
  if (type(i) == int):
    total += i

  else:
   
    for x in i:
     total=total+x
 return (total)



print (nestedsum([1,[5,5,10],6,7]))
