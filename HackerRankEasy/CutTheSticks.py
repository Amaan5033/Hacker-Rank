

def cutTheSticks(arr):
    list=[]
    list.append(len(arr))
    arr.sort(reverse=True)
    while len(arr)>1:
        last_element=arr[-1]
        for i in range(len(arr)-1,-1,-1):
            arr[i]=arr[i]-last_element
            if arr[i]==0:
                index=i
        arr=arr[:index]
        if arr:
            list.append(len(arr))
    return list



n=int(input("Enter the size of array: "))
arr=list(map(int,input("Enter the arr ele: ").rstrip().split()))[:n]
print(cutTheSticks(arr))

