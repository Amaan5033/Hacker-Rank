


def minimumDistances(a):
    mindistance=float("inf")
    dict={}
    for i in range(len(a)):
        if a[i] not in dict:
            dict[a[i]]=[i]
        else:
            dict[a[i]].append(i)
    for i in dict:
        list=dict[i]
        if len(dict[i])==1:
            continue
        elif len(dict[i])%2==0:
            second_index=int(len(dict[i])/2)
            first_index=second_index-1
            value=list[second_index]-list[first_index]
            if value<mindistance:
                mindistance=value
        else:
            mid_index=int(len(dict[i])/2)
            before_index=mid_index-1
            after_index=mid_index+1
            minvalue=min((list[mid_index]-list[before_index]),(list[after_index]-list[mid_index]))
            if minvalue<mindistance:
                mindistance=minvalue
    if mindistance!=float("inf"):
        return mindistance
    else:
        return -1



n=int(input("Enter the size of an array: "))
a=list(map(int,input("Enter the elements: ").rstrip().split()))[:n]
print(minimumDistances(a))
