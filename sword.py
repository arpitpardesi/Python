import math
a=int(input())
r=1
if(a%2==0):
   if(math.sqrt(a)%2==0):
       r=1
   else:
        r=a-1
else:
    if(a==1):
        r=1
    else:
        r=a-2   
print(r)
    