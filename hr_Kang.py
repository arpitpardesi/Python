#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    k1,k2=x1,x2
    x,y=0,0`
    while x!=1:
        k1+=v1
        k2+=v2
        y+=1
        print("Jump %d: %d  %d" %(y,k1,k2))
        if(k1==k2):
            x=1`
        if (y==x2):
            break

    if(x==1):
        return "YES"
    else:
        return "NO"    



if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print (result)
