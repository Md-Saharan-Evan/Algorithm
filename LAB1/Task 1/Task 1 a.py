with open("input1a.txt","r") as file:
   # print(file.read())
    with open("output1a.txt","w") as output:

        T = int(file.readline())
        for i in range(T):
            number=int(file.readline())
            if number%2==0:
                output.write("{} is even number.\n".format(number))
            else:
                output.write("{} is odd number.\n".format(number))


with open("output1a.txt","r") as file_test:
    print(file_test.read())