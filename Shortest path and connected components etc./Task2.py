def no_of_task(sorted_array, n, m):
    selected = []
    sorted_array = sorted(sorted_array, key=lambda array: array[1])
    selected.append(sorted_array[0])
    counter = 0
    task = [0] * n

    for j in range(m):
        current_finish_time = 0
        for i in range(n):
            if sorted_array[i][0] >= current_finish_time and task[i] == 0:
                counter = counter + 1
                current_finish_time = sorted_array[i][1]
                task[i] = 1

    output.write(str(counter))


file = open('input2.txt', 'r')
output = open('output2.txt', 'w')
n, m = map(int, file.readline().split())
array = []
for i in range(n):
    a, b = map(int, file.readline().split())
    updated_list = [a, b]
    array.append(updated_list)

no_of_task(array, n, m)
