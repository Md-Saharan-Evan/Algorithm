with open("input4.txt", "r") as file:
    with open("output4.txt", "w") as output:
        line = file.readline().split()
        nodes, edges = int(line[0]), int(line[1])
        graph = {}
        for i in range(1, nodes + 1):
            graph.update({i: []})
        for j in range(edges):
            read = file.readline().split()
            read = [int(j) for j in read]
            adj = graph.get(read[0])
            adj.append(read[1])
        temp = 0
        for k, nodes in graph.items():
            visit = [k]
            Q = [k]
        while True:
            U = Q.pop(0)
            for vertex in graph[U]:
                if vertex == k:
                    temp = temp + 1
                if vertex not in visit:
                    visit.append(vertex)
                    Q.append(vertex)
            if Q == []:
                break
        if (temp != 0):
            output.write('" YES! "')
        else:
            output.write('" NOO! "')