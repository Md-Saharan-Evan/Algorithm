import math
def mini_titans(graph, source):
  temp =  [math.inf]*len(graph)
  store = [None]*len(graph)
  temp[source] = 0
  queue = [source]
  while len(queue) != 0:
    u = queue.pop(0)
    for vtx in range(len(graph[u])):
      if temp[u] + graph[u][vtx] < temp[vtx] and graph[u][vtx] != 0:
        temp[vtx] = temp[u] + graph[u][vtx]
        store[vtx]= u
        queue.append(vtx)
  return temp, store
file = open('input3.txt', 'r')
output=open('output3.txt',"w")
T = int(file.readline())
for i in range(T):
  node, edge = map(int, file.readline().strip().split())
  graph = [[0 for _ in range(node+1)] for _ in range(node+1)]
  erenLoc = 1
  erenDest = node
  if edge == 0:
    output.write(str(node)+"\n")
  elif edge == 1:
    place1, place2, titans= map(int, file.readline().strip().split())
    output.write(str(place1) + ' -> ' + str(place2)+"\n")
  else:
    for i in range(edge):
      place1, place2, titans= map(int, file.readline().strip().split())
      graph[place1][place2] = titans
      graph[place2][place1] = titans
    dest, prev_road = mini_titans(graph, erenLoc)
    path = str(erenDest)
    end = erenDest
    while end != erenLoc:
      path = str(prev_road[end]) + ' -> ' + path
      end = prev_road[end]
    output.write(str(path))