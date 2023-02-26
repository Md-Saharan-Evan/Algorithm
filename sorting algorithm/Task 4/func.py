

def queue(lst):
    for i in range(len(list1)):
        a,b=list1[i].split(" ")
        for j in range(i+1,len(list1)):
            c,d=list1[j].split(" ")
            if b>d:
                list1[i],list1[j]=list1[j],list1[i]
    return list1
def seeDoct(a):
    poped,val=list1.pop(0).split(" ")
    return("Name:",poped)  ##i'm getting output because i have poped the first element of queue

def printqueue(list1):
    print(seeDoct(list1))
    print(queue(list1))
    
with open("input.txt","r") as file:
    list1=[]
    elem=file.readline()
    while elem!="":
        
        elem=elem.strip()
        if elem=="see doctor":
            #seeDoct(list1)
            printqueue(list1)
        else:
            list1.append(elem)
            #a,b=elem.split(" ")
            queue(list1)
                        
        #print(list1)
        elem=file.readline()