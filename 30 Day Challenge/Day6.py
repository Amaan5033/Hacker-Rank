


a=int(input())
for i in range(a):
    b=str(input())
    for i in range(len(b)):
        if i==0 or i%2==0:
            print(b[i],end="")
    print(" ",end="")
    for i in range(len(b)):
        if i!=0 and i%2!=0:
            print(b[i],end="")
    print("\n")