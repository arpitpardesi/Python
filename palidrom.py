def reve(num):
    rev = 0
    while (num > 0):
        b = num%10
        rev = (rev*10) + b
        num = num//10
    return rev

a = input()
a = int(a)
b = reve(a)
while(a != b):
    a = a + b
    b = reve(a)
print(a)