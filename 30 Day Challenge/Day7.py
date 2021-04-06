



#!/bin/python3

import math
import os
import random
import re
import sys

def ReverseArray(arr):
    for i in range(len(arr)-1,-1,-1):
        print(arr[i],end=" ")



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    ReverseArray(arr)