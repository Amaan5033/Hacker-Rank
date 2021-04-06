
import sys

def stringToInteger(S):
    try:
        S=int(S)
        print(S)
    except:
        print("Bad String")



S = input().strip()
stringToInteger(S)


