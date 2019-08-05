import sys
a = sys.argv[0]
b = ['defer','continue','if','else',
     'return','break','const','for','goto']
if a in b:
    print(a + " is a keyword")
else:
    print(a + " is a not keyword")