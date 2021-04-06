


import math
import os
import random
import re
import sys



def Getnames(firstName,emailID):
    pattern=re.compile(r"\bgmail.com")
    matches=pattern.search(emailID)
    if matches:
        return firstName
    


if __name__ == '__main__':
    li=[]
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split(" ")
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        names=Getnames(firstName,emailID)
        if names:
            li.append(names)

li.sort()
for i in li:
    print(i)