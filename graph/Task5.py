import math
def computer(graph, source):
  temp =  [-1]*len(graph)
  store = [[] for a in range(len(graph))]
  temp[0] = math.inf
  temp[source] = 0
  queue = [source]
  while len(queue) != 0:
    u = queue.pop(0)
    for vtx in range(len(graph[u])):
      if graph[u][vtx] != 0:
        if temp[u] != 0:
          alt = min(temp[u], graph[u][vtx])
        else:
          alt = max(temp[u], graph[u][vtx])
        store[vtx].append(u)
        if alt > temp[vtx]:
          temp[vtx] = alt
          queue.append(vtx)
  return temp, store
file = open('input5.txt', 'r')
T = int(file.readline())
output=open("output5.txt","w")
for i in range(T):
  node, edge = map(int, file.readline().strip().split())
  graph = [[0 for a in range(node+1)] for a in range(node+1)]
  if edge == 0:
    started = int(file.readline())
    output.write(str(0)+"\n")
  else:
    for i in range(edge):
      vertex1, vertex2, speed = map(int, file.readline().strip().split())
      graph[vertex1][vertex2] = speed
    started = int(file.readline())
    final, prev_connection = computer(graph, started)
    for i in range(1, len(final)):
      output.write(str(final[i])+" ")
    output.write("\n")