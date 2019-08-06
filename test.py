a = input().split()
e = []
q = ['0','00','000','0000','00000','000000','0000000','00000000','0000000000','0000000000']
c = q[len(a[1])-1]
for i in range(int(a[0]),int(a[1])+1):
    f = c + str(i)
    #f = q[len(str(i))-1] + str(i)
    print(f,end=" ")