import math
class Graph:
    def __init__(self,vertex,target):
        self.V=vertex
        self.t=target
        self.graph={}
        self.dist={}
        self.par={}
        self.start='1'
        self.temp=self.t
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
    
    def __str__(self) -> str:
        print(self.graph)
    def shortest_time(self):
        self.path=str(self.t)
        self.Q=[]
        self.rslt=""
        for keys in self.graph.keys():
           
            self.dist[keys]=math.inf
        self.dist['1']=0
        self.Q.append('1')
        while self.Q:
            self.u=self.Q.pop(0)
            for j in self.graph[self.u]:
                if self.dist[str(j)]==math.inf:
                    self.dist[str(j)]=self.dist[self.u]+1
                    self.Q.append(str(j))
                    self.par[str(j)]=self.u
        while str(self.t)!=str(self.start):
            for j,k in self.par.items():
                if self.t==j:
                    self.t=self.par[j]
                    self.path+=str(self.par[j])
        #print(self.path)
        #print(self.dist)
        with open("output5.txt","w") as output:
            for x, y in self.dist.items():
                if x == self.temp:
                    output.write("Time taken: {}\n".format(y))
            for a in range(len(self.path) - 1, -1, -1):
                self.rslt+=self.path[a]+","
            output.write("shortest path:{}".format(self.rslt))



with open("input5.txt","r") as file:
    T=file.readline().split(" ")
    e=int(T[1])
    v=T[0]
    t=T[2]
    t=t.strip("\n")
    grp=Graph(v,t)
    for i in range(e):
        store=file.readline().split(" ")
        a,b=store[0].strip(),store[1].strip("\n")
        grp.edges(a,b)
    #grp.__str__()


    grp.shortest_time()


     

    