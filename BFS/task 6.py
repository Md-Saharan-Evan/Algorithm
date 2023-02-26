with open("input6.txt","r") as file:
    with open("output6.txt","w") as output:
        T=file.readline().split()
        List=[]
        collected={}
        #collect=0
        for a in range(int(T[0])):
            line=file.readline()
            List.append([])
            for i in range(int(T[1].strip("\n"))):
                List[a].append(line[i].strip())
        #print(List)
        def up(row,diamond):
            if row<0:
                return 0
            else:
                if List[row][diamond]==".":
                    up(row-1,diamond)
                if List[row][diamond]=="D":
                    return 1+up(row-1,diamond)
        def down(row,diamond):
            if row>= len(List):
                return 0
            else:
                if List[row][diamond] == ".":
                    up(row + 1, diamond)
                if List[row][diamond] == "D":
                    return 1 + up(row + 1, diamond)
        def right(row,diamond):
            if List[row][diamond+1]==".":
                right(row,diamond+1)
                if List[row-1]<0 or List[row-1][diamond]=="#":
                    pass
                else:
                   p= down(row+1,diamond)
                if List[row+1]>=len(List) or List[row+1][diamond]=="#":
                    pass
                else:
                    q=p+up(row-1,diamond)
            if List[row][diamond+1]=="D":
                List[row][diamond+1]=1
                if List[row-1]<0 or List[row-1][diamond]=="#":
                    pass
                else:
                   r= down(row+1,diamond)
                if List[row+1]>=len(List) or List[row+1][diamond]=="#":
                    pass
                else:
                    s=r+up(row-1,diamond)
                return p+q+r+s+1+right(row,diamond+1)

        def left(row,diamond):
            if List[row][diamond - 1] == ".":
                left(row, diamond - 1)
                if row - 1 < 0 or List[row - 1][diamond] == "#":
                    pass
                else:
                    p = down(row + 1, diamond)
                if row + 1 >= len(List) or List[row + 1][diamond] == "#":
                    pass
                else:
                    q = p + up(row - 1, diamond)
            if List[row][diamond -1] == "D":
                List[row][diamond - 1] = 1
                if row - 1 < 0 or List[row - 1][diamond] == "#":
                    pass
                else:
                    r = down(row + 1, diamond)
                if row + 1 >= len(List) or List[row + 1][diamond] == "#":
                    pass
                else:
                    s = r + up(row - 1, diamond)
                return p + q + r + s + 1 + right(row, diamond + 1)
        def search(row,position):
           for a in range(len(List)):
               for b in range(len(List[a])):
                   collect=0
                   if List[a][b]=="D":
                       collect+=1
                       List[a][b]=1
                       #right(a,b+1)
                       if b-1<0 or List[a][b-1]=="#":
                           pass

                       else:
                           return 1 + left(a,b-1)
                       if b+1>=len(List[a]) or List[a][b+1]=="#":
                           pass
                       else:
                           return collect+right(a,b+1)
                   else:
                      
                       print("No diamond")
              
        print(search(0,0))
