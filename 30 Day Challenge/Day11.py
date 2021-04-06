


def maximumvaluehourglass(arr):
    max_value=[]
    for i in range(len(arr)-2):
        sum=0
        for j in range(len(arr[i])-2):
            sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            max_value.append(sum)
    return max(max_value)


# arr=[[1, 1, 1, 0, 0, 0],
#      [0, 1, 0, 0, 0, 0],
#      [1, 1, 1, 0, 0, 0],
#      [0, 0, 2, 4, 4, 0],
#      [0, 0, 0, 2, 0, 0],
#      [0, 0, 1, 2, 4, 0]]

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(maximumvaluehourglass(arr))