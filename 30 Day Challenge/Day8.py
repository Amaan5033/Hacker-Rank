


# Enter your code here. Read input from STDIN. Print output to STDOUT

# def searchPhonebook(dict,name):
#     if name not in dict:
#         print("Not found")
#     else:
#         print(f"{name}={dict[name]}")

# if __name__=="__main__":
#     N=int(input())
#     dict={}
#     for i in range(N):
#         name=input()
#         PhoneNumber=int(input())
#         dict[name]=PhoneNumber
#     searchPhonebook(dict,name)

# phonebook={("sam","99912222"),("tom",11122222),("harry",122999333)}

# for i in range(phonebook):
#     if [i][0]==


# N=int(input("No of integer "))
# phonebook=set()
# for i in range(N):
#     b=input("Name of record ")
#     phonebook.add(tuple(b.split()))
# for i in range(N):
#     c=input("Name of query ")
#     count=0
#     for i in phonebook:
#         if i[0]==c:
#             print(f"{c}={i[1]}")
#             break
#         count+=1
#     if count==len(phonebook):
#         print("Not found")
        

# print(phonebook)

# Using dictionary

# N=int(input("No of integer "))
# phonebook={}
# for i in range(N):
#     b=input("Name of record ")
#     b=b.split()
#     for i in range(1):
#         phonebook[b[i]]=int(b[i+1])
# for i in range(N):
#     c=input("Name of query ")
#     # try:
#     #     print(f"{c}={phonebook[c]}")
#     # except:
#     #     print("Not found")
#     if c in phonebook:
#         print(f"{c}={phonebook[c]}")
#     else:
#         print("Not found")


n=int(input())
phonebook={}
for i in range(n):
    l1 = list(map(str,input().split()))
    key =l1[0]
    value=l1[1]
    phonebook[key]=value

while True:
    try:
        name=input()
        if name in phonebook:
            print(name+"="+phonebook[name])
        else:
            print("Not found")
    except:
        break