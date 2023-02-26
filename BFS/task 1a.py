# task 1a
file = open("input1a.txt", "r")
line = file.readline().split(" ")

def Int(arr):
  for i in range(len(arr)):
    arr[i] = int(arr[i])
  return arr

List = Int(line)
Array = []
for j in range(List[0]+1):
  tamp = [0]*(List[0]+1)
  Array.append(tamp)

i =1
while List[0]>i:
  lin_red_by = Int(file.readline().split(" "))
  Array[lin_red_by[0]][lin_red_by[1]] = lin_red_by[2]
  i +=1

output = open("output1a.txt", "w")

for a in Array:
  for b in a:
    output.write("{} ".format(b))
  output.write("\n")