with open("input1.txt","r") as file:
    T=file.readline()
    T=int(T)
    store=[]
    for i in range(T):
        start,end=file.readline().split(" ")
        end=end.strip("\n")
        start=start.strip()
        store.append([start,end])
    for i in range(len(store)):
        for j in range(i,len(store)):
            if int(store[i][1])>=int(store[j][1]):
                store[i],store[j]=store[j],store[i]
    counter=1
    list=[]
    temp=store[0][1]
    list.append(store[0])
    output = open('output1.txt', 'w')
    for i in range(1,len(store)):
        if int(temp)<=int(store[i][0]):
            list.append(store[i])
            counter+=1
            temp=store[i][1]
    output.write(str(counter))
