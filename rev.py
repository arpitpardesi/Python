a = input()
c = 0
d = []
for i in a:
    
    if(i == '0'):
        print("contains zero")
        break
    elif(i != '0'):
        c = c+1
        if(c>2):
            print("Not a 2 digit number")
        else:
            d.append(i)
if(c==2):
    print(d[1],d[0],sep="")
