def square_number(a, b):
    count = 0
    for i in range(a, b + 1):
        j = 1
        while j * j <= i:
            if j * j == i:
                count = count + 1
            j = j + 1
        i = i + 1
    return count
file = open('input4.txt', 'r')
output = open('output4.txt', 'w')
list1 = file.read().split("\n")
store = []
for i in list1:
    temp = []
    for j in i.split(" "):
        temp.append(int(j))
    store.append(temp)

for i in store:
    if i[0] != 0 and i[1] != 0:
        output.write(str(square_number(i[0], i[1])) + "\n")
