def google(b,x):
    if (b[0]=='g' or b[0]=='G'):
        if (b[1]=='o' or b[1]=='0' or b[1]=='O' or b[1]=='()' or b[1]=='[]' or b[1]=='<>'):
            if (b[2]=='o' or b[2]=='0' or b[2]=='O' or b[2]=='()' or b[2]=='[]' or b[2]=='<>'):
                if (b[3]=='g' or b[3]=='G'):
                    if (b[4]=='l' or b[4]=='L' or b[4]=='I'):
                        if(b[5]=='e' or b[5]=='3' or b[5]=='E'):
                            if(b[6]=='e' or b[6]=='3' or b[6]=='E'):
                                return False
                            elif(x!=0):
                                return False
                            else:
                                x+=1
                                return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False                
    else:
        return False

string = input()
x=0
b=['','','','','','','','','','','']
c=['','','','','','','']
for i in string:
    b[x]=i
    x+=1
print(b)
c[0]=b[0]
if((b[1]=='(' and b[2]==')' ) or (b[1]=='<' and b[2]=='>' ) or (b[1]=='[' and b[2]==']' )):
    c[1]=b[1]+b[2]
    if((b[3]=='(' and b[4]==')' ) or (b[3]=='<' and b[4]=='>' ) or (b[3]=='[' and b[4]==']' )):
        c[2]=b[3]+b[4]
        c[3]=b[5]
        c[4]=b[6]
        c[5]=b[7]
    else:
        c[2]=b[3]
        c[3]=b[4]
        c[4]=b[5]
        c[5]=b[6]
else:
    c[1]=b[1]
    c[2]=b[2]
    c[3]=b[3]
    c[4]=b[4]
    c[5]=b[5]
    x=0
    c[6]=b[6]
    
print(c)     
print(google(c,x))


