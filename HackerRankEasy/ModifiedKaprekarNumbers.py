


def kaprekarNumbers(p,q):
    list=[]
    for i in range(p,q+1):
        n=i**2
        n=str(n)
        if i==1:
            list.append(i)
            continue
        if len(n)!=1:
            r=n[len(n)-len(str(i)):]
            l=n[:len(n)-len(str(i))]
            r=int(r)
            l=int(l)
            sum=l+r
            if sum==i:
                list.append(i)
    if list:
        for i in list:
            print(i,end=" ")
    else:
        print("INVALID RANGE")




p=int(input("Enter the lower integer limit: "))
q=int(input("Enter the upper integer limit: "))
kaprekarNumbers(p,q)