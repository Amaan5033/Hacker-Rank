


def rotate(list):
    rotatelist=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            rotatelist[2-j][i]=list[i][j]
    return rotatelist

def mirror(list):
    mirrorlist=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            mirrorlist[i][2-j]=list[i][j]
    return mirrorlist




def formingMagicSquare(s):
    knownSquare=[[6,1,8],[7,5,3],[2,9,4]]
    allmagicSquare={1:knownSquare}
    afterrotation=knownSquare
    count=2
    for i in range(3):
        afterrotation=rotate(afterrotation)
        allmagicSquare[count]=afterrotation
        count+=1
    aftermirror=mirror(knownSquare)
    allmagicSquare[count]=aftermirror
    count+=1
    knownsquare=aftermirror
    for i in range(3):
        knownsquare=rotate(knownsquare)
        allmagicSquare[count]=knownsquare
        count+=1
    
    mincost=float("inf")
    for i in allmagicSquare:
        value=allmagicSquare[i]
        cost=0
        for i in range(3):
            for j in range(3):
                if value[i][j]!=s[i][j]:
                    cost+=abs(value[i][j]-s[i][j])
        if cost<mincost:
            mincost=cost

    return mincost
            

    




s=[]
for i in range(3):
    values=list(map(int,input("Enter the values: ").rstrip().split()))[:3]
    s.append(values)  
print(formingMagicSquare(s))
