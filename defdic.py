"""

Program to find position of given input items from a given input string and print position of each item in separate line

"""
a,b = [],[]
inp = input().split()
for i in range(0,int(inp[0])):
    c = input()
    a.append(c)
for i in range(0, int(inp[1])):
    d = input()
    b.append(d)
c,d= [], []
for i in range(0, int(inp[1])):
    co=0
    for j in range(0,int(inp[0])):
        if (b[i] == a[j]):
            d.append(j+1)
            co = co + 1
    c.append(co)
e,f=0,0
for i in range(0,len(c)):
    f = f + c[i]
    if(f<=len(d)):
        for j in range(e,f):
            print(d[j],end=' ')
        e = e + c[i]
    print("")        