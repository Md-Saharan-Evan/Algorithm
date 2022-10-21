with open("input1b.txt","r") as file:
    with open("output1b.txt","w") as out:
        T=int(file.readline())
        for i in range(T):
            temp=file.readline().split(" ")
            if temp[2]=="+":
                out.write("The result of {fisrt} {opr} {second} is {result}\n".format(fisrt=temp[1],opr=temp[2],second=temp[3],result=int(temp[1])+int(temp[3])))
            elif temp[2]=="-":
                out.write("The result of {fisrt} {opr} {second} is {result}\n".format(fisrt=temp[1], opr=temp[2],
                                                                                      second=temp[3],
                                                                                      result=int(temp[1]) - int(temp[3])))
            elif temp[2]=="*":
                out.write("The result of {fisrt} {opr} {second} is {result}\n".format(fisrt=temp[1], opr=temp[2],
                                                                                      second=temp[3],
                                                                                      result=int(temp[1]) * int(temp[3])))
            else:
                out.write("The result of {fisrt} {opr} {second} is {result}\n".format(fisrt=temp[1], opr=temp[2],
                                                                                      second=temp[3],
                                                                                      result=int(temp[1])/int(temp[3])))

with open("output1b.txt") as file_test:
    print(file_test.read())