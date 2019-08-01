#            CTL Cup - 2019            #    
a=int(input("Enter no. of peoples: "))
for i in range(0,a):
    b=2**i
    if(b>a):
        c=i-1
        break
    elif(b==a):
        c=i
        break
print("Last alive: "+str((2*(a-2**c)+1)))
