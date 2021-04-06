

def getTwoPowers(n):
    if n==0:
        return [1]
    if n==1:
        return [0]
    li=[]
    i=1
    count=0
    while i<n:
        count+=1
        i=i*2
    if i==n:
        li.append(count)
        return li
    else:
        i=int(i/2)
        li.append(count-1)
        return li+getTwoPowers(n-i)


def binaryconversion(n):
    a=getTwoPowers(n)
    if a[-1]!=0:
        for i in range(a[-1]):
            a.append(0)
    c=0
    string=""
    for i in range(a[0],-1,-1):
        if a[c]==i:
            string+="1"
            c+=1  
        else:
            string+="0"
    if n%2==0:
        string=string[:-1]+"0"
    count_list=[]
    count=0
    for i in string:
        if i=="1":
            count+=1
        else:
            count_list.append(count)
            count=0
    if string[-1]=="1":
        count_list.append(count)
    if "0" not in string:
        return count
    else:
        return max(count_list)


n=int(input("Enter the number: "))
print(binaryconversion(n))





