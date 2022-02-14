

from collections import Counter
def acmTeam(topic):
    maxteam=0
    maxtopic=0
    for i in range(len(topic)):
        for j in range(i+1,len(topic)):
            value=int(topic[i],2)|int(topic[j],2)
            value=bin(value).replace("0b","")
            count=Counter(value)
            if count["1"]>maxtopic:
                maxtopic=count["1"]
                maxteam=1
            elif count["1"]==maxtopic:
                maxteam+=1
    return [maxtopic,maxteam]


first_input=list(map(int,input("Enter the n and m value: ").rstrip().split()))
n=first_input[0]
m=first_input[1]
topic=[]
for i in range(n):
    topic_team=input("Enter the topic: ")[:m]
    topic.append(topic_team)
print(acmTeam(topic))