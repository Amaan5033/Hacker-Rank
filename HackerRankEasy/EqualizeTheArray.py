

from collections import Counter
def equalizeArray(arr):
    count=Counter(arr)
    maxcount=0
    sum=0
    for i in count:
        if count[i]>maxcount:
            sum+=maxcount
            maxcount=count[i]
        else:
            sum+=count[i]
    return sum




n=int(input("Enter the number of elements: "))
arr=list(map(int,input().rstrip().split()))[:n]
print(equalizeArray(arr))