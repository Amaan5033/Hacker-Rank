

import math
import os
import random
import re
import sys


def ConditionalStatement(N):
    if N>=1 and N<=100:
        if N%2!=0:
            print("Weird")
        if N%2==0 and (N>=2 and N<=5):
            print("Not Weird")
        if N%2==0 and (N>=6 and N<=20):
            print("Weird")
        if N%2==0 and N>20:
            print("Not Weird")
    
    



if __name__ == '__main__':
    N = int(input())
    ConditionalStatement(N)