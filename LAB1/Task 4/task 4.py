with open("input.txt","r") as file:
    N=int(file.readline())


    list=file.readline().split(" ")
    list2=file.readline().split(" ")

    if len(list)!=N or len(list2)!=N:
        print("incorrect input")

    else:
        for i in range(len(list2) - 1):
            for j in range(i + 1, len(list2)):
                if int(list2[i]) < int(list2[j]):
                    list2[i]=int(list2[i])
                    list[i]=int(list[i])
                elif int(list2[i]) == int(list2[j]):
                    if int(list[i]) > int(list[j]):
                        list2[i]=int(list2[i])
                        list[i]=int(list[i])
                    else:
                        temp = int(list2[i])
                        list2[i] = int(list2[j])
                        list2[j] = temp
                        temp1 = int(list[i])
                        
                        list[i] = int(list[j])
                        list[j] = temp1
                else:
                    temp = int(list2[i])
                    list2[i] = int(list2[j])
                    list2[j] = temp
                    temp1 = int(list[i])
                    
                    list[i] = int(list[j])
                    list[j] = temp1

    for a in range(len(list) - 1, -1, -1):
        print("ID:{} Mark:{}".format(list[a], list2[a]))
    with open("output.txt","w") as output:
        for a in range(len(list)-1,-1,-1):
            output.write("ID:{} Mark:{}\n".format(list[a], list2[a]))
    