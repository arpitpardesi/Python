a=input()
#a=a.split()
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b=[]
for i in a:
    b+=i
print(b)
c=[]
for i in range(0,len(b)):
    for j in range(0,len(al)):
        if(b[i]==al[j]):
            print(j)
