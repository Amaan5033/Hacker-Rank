

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    max=0
    for i in range(1,N+1):
        if i==K:
            break
        else:
            for j in range(i+1,N+1):
                if i&j==i:
                    max=i
                    break
                else:
                    if i&j>max and i&j<K:
                        max=i&j             
    return max
            

if __name__ == '__main__':    
    t = int(input().strip())
    li=[]
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)
        
        li.append(res)


for i in li:
    print(i)

        


