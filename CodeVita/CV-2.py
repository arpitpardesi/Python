n = int(input())
s = input()
q = int(input())
a = []
c = []
for i in range(0, q):
    a.append(input())
    c.append(s[int(a[i])-1])
    flag = 0
    for j in range(0, int(a[i])-1):
        if(s[j] == c[i]):
            flag = flag +1
    print(flag)
