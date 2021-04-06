
import sys

def BubbleSort(a):
    j,b=0,1
    num_of_Swaps=0
    while j<len(a):
        i=0
        while i<len(a)-b:
            if a[i]>a[i+1]:
                num_of_Swaps+=1
                a[i],a[i+1]=a[i+1],a[i]
            i+=1
        b+=1
        j+=1
    print(f"Array is sorted in {num_of_Swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")        


# a=[5,9,3,1,2,8,4,7,6]
# a=[4,3,1,2]
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
BubbleSort(a)
# Write Your Code Here


