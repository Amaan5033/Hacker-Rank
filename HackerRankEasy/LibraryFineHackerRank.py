

def libraryFine(d1,m1,y1,d2,m2,y2):
    fine=0
    days={1:31,2:28,3:31,4:30,5:31,6:30,
          7:31,8:31,9:30,10:31,11:31,12:31}
    if y1%400==0:
        days[2]=29
    elif y1%100!=0 and y1%4==0:
        days[2]=29
    if m1==m2 and y1==y2 and (d1-d2)>0:
        fine+=15*(d1-d2)
    elif y1==y2 and (m1-m2)>0:
        fine+=500*(m1-m2)
    elif y1!=y2 and y1>y2:
        fine+=10000
    return fine





issuedate=list(map(int,input("Enter the return date: ").rstrip().split()))
duedate=list(map(int,input("Enter the due date: ").strip().split()))
d1,m1,y1=issuedate[0],issuedate[1],issuedate[2]
d2,m2,y2=duedate[0],duedate[1],duedate[2]
print(libraryFine(d1,m1,y1,d2,m2,y2))