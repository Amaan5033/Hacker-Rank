
import math

def encryption(s):
    s=s.replace(" ","")
    L=len(s)
    column=math.ceil(math.sqrt(L))
    rows=math.floor(math.sqrt(L))
    if (rows*column)<L:
        rows=rows+1
    matrix=[["" for i in range(column)] for j in range(rows)]
    count=0
    for i in range(rows):
        for j in range(column):
            if count<L:
                matrix[i][j]=s[count]
                count+=1
    encodedstr=""
    for i in range(column):
        str=""
        for j in range(rows):
            str+=matrix[j][i]
        encodedstr=encodedstr+str+" "
    return encodedstr
    


s=input("Enter the String: ")
print(encryption(s))