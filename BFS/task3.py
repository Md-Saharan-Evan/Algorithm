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
        
    def DFS(self,sorc):
        self.src=sorc
        self.visit=set()
        self.stack=[]
        self.temp=""
        self.stack.append(self.src)
        while (len(self.stack)):
            u=self.stack.pop()
            if u not in self.visit:
                #print(u,end=" ")
                self.temp+="{} ".format(u)
                self.visit.add(u)
            if u not in self.graph:
                continue
            else:
                for node in self.graph[u]:
                    if node not in self.visit:
                        #self.visit.add(node)
                        self.stack.append(node)
        with open("output3.txt","w") as output:
            output.write(self.temp)

    def __str__(self) -> str:
        print(self.graph)
with open("input3.txt","r") as file:
    T=file.readline().split(" ")
    e=int(T[1])
    v=T[0]
    grp=Graph(v)
    for i in range(e):
        store=file.readline().split(" ")
        a,b=store[0].strip(),store[1].strip("\n")
        grp.edges(a,b)
    #grp.__str__()

    grp.DFS("1")


     

    