class Graph:
    def __init__(self,vertex):
        self.V=vertex
        self.graph={}
    def edges(self,source,destinition):
        self.src=source
        self.dst=destinition
        if self.graph.get(self.src)==None:
            self.graph[self.src]=[self.dst]
        else:
            self.graph[self.src]+=[self.dst]
        if self.graph.get(self.dst)==None:
            self.graph[self.dst]=[self.src]
        else:
            self.graph[self.dst]+=[self.src]
        
    def BFS(self,sorc):
        self.s=sorc
        self.visit=set()
        self.Q=[]
        self.st=""
        self.visit.add(self.s)
        self.Q.append(self.s)
        while self.Q:
            self.s=self.Q.pop(0)


            print(self.s,end=" ")
            self.st+="{} ".format(self.s)
            if self.s not in self.graph:
                continue
            else:
                for node in self.graph[self.s]:
                    if node not in self.visit:
                        self.visit.add(node)
                        self.Q.append(node)
        with open("output2.txt", "w") as output:
            output.write(self.st)

    def __str__(self) -> str:
        with open("output.txt","w") as output:
            output.write(self.graph)
        print(self.graph)
with open("input2.txt","r") as file:
    T=file.readline().split(" ")
    e=int(T[1])
    v=int(T[0])
    grp=Graph(v)
    for i in range(e):
        store=file.readline().split(" ")
        a,b=store[0].strip(),store[1].strip("\n")
        grp.edges(a,b)
    #grp.__str__()

    grp.BFS("1")

     

    