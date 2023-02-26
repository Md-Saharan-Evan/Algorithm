class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}
        self.blocked = []
    def add_edge(self, src, dest, weight):
        if self.graph.get(src) == None:
            self.graph[src] = [(dest, weight)]
        else:
            self.graph[src] = self.graph.get(src) + [(dest, weight)]
    def dijkstra(self, src, dst=None):
        vertices = []
        for n in self.graph:
            vertices.append(n)
            for v in self.graph[n]:
                vertices += [v[0]]
        queue = set(vertices)
        vertices = list(queue)
        dist = {}
        prev = {}
        for n in vertices:
            dist[n] = float('inf')
            prev[n] = None
        dist[src] = 0
        while queue:
            u = min(queue, key=dist.get)
            queue.remove(u)
            if dst is not None and u == dst:
                return dist[dst], prev
            for v, w in self.graph.get(u, ()):
                if v in self.blocked:
                    w = float('inf')
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
        return dist, prev
    def find_path(self, pr, vert):
        rev = []
        while vert is not None:
            rev.append(vert)
            vert = pr[vert]
        return rev[::-1]
with open("input1.txt","r") as file:
    T=file.readline().split(" ")
    N = int(T[0].strip())
    M = int(T[1].strip("\n"))
    myGraph = Graph(N)
    for i in range(M):
        u,v,w=file.readline().split()
        u=u.strip()
        v=v.strip()
        w=int(w.strip("\n"))
        myGraph.add_edge(u, v, w)
    src ="Motijheel" 
    dest = "MOGHBAZAR"
    cost, prev = myGraph.dijkstra(src, dest)
    path = myGraph.find_path(prev, dest)
    dest_name="MOGHBAZAR"
    output=open("output1.txt","w")
    output.write(str(cost))
