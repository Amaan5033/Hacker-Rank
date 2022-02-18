

def beautifulTriplets(d,arr):
    count=0
    for i in range(len(arr)-2):
        j=i+1
        k=j+1
        while k<len(arr) and (arr[j]-arr[i])<=d:
            if (arr[j]-arr[i])<(arr[k]-arr[j]):
                j+=1
                k=j+1
            elif (arr[j]-arr[i])==d and (arr[k]-arr[j])==d:
                count+=1 
                k+=1
            elif (arr[j]-arr[i])>=(arr[k]-arr[j]):
                k+=1 
            else:
                break
    return count
            



first_input=list(map(int,input("n and d: ").rstrip().split()))
n=first_input[0]
d=first_input[1]
arr=list(map(int,input("Enter the elements: ").rstrip().split()))[:n]
print(beautifulTriplets(d,arr))