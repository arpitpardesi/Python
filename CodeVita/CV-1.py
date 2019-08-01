h = int(input())
c=0
dh = input().split(" ")
m = int(input())
db = input().split(" ")
db.reverse()
for i in range (0,m):
    if(db[i]<=dh[i]):
        c=c+1
print(c)