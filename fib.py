def fib (n):
    fibresult = []
    fibresult[0] = 1
    fibresult[1] = 1
    for i in range(2,n):
        fibresult[i] = fibresult[i-1] + fibresult[i-2]

a=input()
fib(a)