with open("input1b.txt","r") as file:
    T=file.readline().split(" ")
    
    dict={}
    
    for i in range(int(T[1])):
        elem=file.readline().split(" ")
        
        for j in range(int(T[0])+1):
            if j not in dict:
                dict[j]=""
            if int(elem[0])==j:
                
                for k in range(int(T[0])+1):
                    if k==int(elem[1]):
                        if j not in dict:
                            dict[j]="({},{}) ".format(k,elem[2].strip("\n"))
                        else:
                            dict[j]+="({},{})".format(k,elem[2].strip("\n"))
    with open("output1b.txt","w") as output:
        for e,f in dict.items():
            output.write("{} : {}\n".format(e, f))
