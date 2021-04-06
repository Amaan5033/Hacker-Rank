
import datetime

def LibraryFine(rdate,ddate):
    rdate=datetime.datetime(rdate[2],rdate[1],rdate[0])
    ddate=datetime.datetime(ddate[2],ddate[1],ddate[0])

    if rdate.strftime("%Y")==ddate.strftime("%Y") and rdate.strftime("%m")==ddate.strftime("%m"):
        if int(rdate.strftime("%d"))<int(ddate.strftime("%d")):
            return 0
        else:
            return 15*(int(rdate.strftime("%d"))-int(ddate.strftime("%d")))

    elif rdate.strftime("%Y")==ddate.strftime("%Y") and rdate.strftime("%m")!=ddate.strftime("%m"):
        if int(rdate.strftime("%m"))<int(ddate.strftime("%m")):
            return 0
        else:
            return 500*(int(rdate.strftime("%m"))-int(ddate.strftime("%m")))

    else:
        if int(rdate.strftime("%Y"))<int(ddate.strftime("%Y")):
            return 0 
        else:
            return 10000
rdate=list(map(int,input().strip().split(" ")))
ddate=list(map(int,input().strip().split(" ")))

print(LibraryFine(rdate,ddate))

