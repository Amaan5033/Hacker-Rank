# Append and Delete
from collections import Counter

def appendAndDelete(s,t,k):
    if (s==t and k%2==0):
        return "Yes" 
    if (s==t and (2*len(s))<=k):
        return "Yes"
    dictS=Counter(s)
    append=0
    delete=0
    for i in t:
        if i in dictS and dictS[i]>0:
            dictS[i]-=1
        else:
            append+=1
    for i in dictS:
        delete+=dictS[i]
    sumofOp=delete+append
    if sumofOp>k:
        return "No"
    elif sumofOp==k:
        return "Yes"
    else:
        diff=k-sumofOp
        if diff%2==0:
            return "Yes"
        else:
            return "No"






def appendAndDelete2(s,t,k):
    ls=len(s)
    lt=len(t)
    flag=0
    if k>=(ls+lt):
        return "Yes"
    if abs(ls-lt)>k:
        return "No"
    minlen=min(ls,lt)
    for i in range(minlen):
        if s[i]!=t[i]:
            flag=1
            break
    if flag==0:
        if (abs(ls-lt)%2!=0 and k%2!=0) or (abs(ls-lt)%2==0 and k%2==0):
            return "Yes"
        else:
            return "No"
    else:
        newS=s[i:]
        newT=t[i:]
        lsn=len(newS)
        ltn=len(newT)
        if ((lsn+ltn)<=k and abs(lsn-ltn)%2!=0 and k%2!=0) or ((lsn+ltn)<=k and abs(lsn-ltn)%2==0 and k%2==0):
            return "Yes"
        else:
            return "No"



s=input("Enter the s string: ")
t=input("Enter the t string: ")
k=int(input("Enter the K value: "))
print(appendAndDelete2(s,t,k))


