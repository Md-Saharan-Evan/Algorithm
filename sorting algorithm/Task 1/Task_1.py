with open("Input.txt","r") as file:
    Imp=int(file.readline())
    Id=file.readline().split(" ")
    Marks=file.readline().split(" ")

    def insertionSort(Imp,Id,Marks):                    ##111 452 343 224 125
                                            # 40 50 20 10 10 
                                            #452 111 343 224 125

        for i in range(Imp):
            for j in range(0,i,1):
                if int(Marks[j])<int(Marks[j+1]):
                    Marks[j],Marks[j+1]=Marks[j+1],Marks[j]
                    Id[j],Id[j+1]=Id[j+1],Id[j]
        with open("output.txt","w") as output:
            for i in Id:
                output.write(i+" ")

    
    insertionSort(Imp,Id,Marks)