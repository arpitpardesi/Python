a=input()
b=[]
for i in a:
    b+=i
print(b)
c=['','','']
#for i in range(0,3):
c[0]=b[0]+b[1]
c[1]=b[2]+b[3]
c[2]=b[4]
print(c)