#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    ar.sort()
    max=ar[-1]
    c=0
    for i in range(0,len(ar)):
        if(max==ar[i]):
            c+=1
    return c


ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
result = birthdayCakeCandles(ar)
print(result)