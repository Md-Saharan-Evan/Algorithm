with open("input.txt","r") as file:
    list1=[]
    elem=file.readline()
    while elem!="":
        
        elem=elem.strip()
        if elem=="see doctor":
            poped,val=list1.pop(0).split(" ")
            print("name:",poped)
        else:
            list1.append(elem)
            #a,b=elem.split(" ")
            for i in range(len(list1)):
                a,b=list1[i].split(" ")
                for j in range(i+1,len(list1)):
                    c,d=list1[j].split(" ")
                    if b>d:
                        list1[i],list1[j]=list1[j],list1[i]
                        
        print(list1)
        elem=file.readline()