def children(n, time, call):
    time.sort()
    jack_task = []
    store = []
    jack_time = 0
    jill_time = 0
    count = 0

    for i in range(len(call)):
        if call[i] == "J":
            jack_task.append(time[count])
            store.append(time[count])
            jack_time = jack_time + time[count]
            count = count + 1

        elif call[i] == "j":
            task_time = jack_task.pop()
            store.append(task_time)
            jill_time = jill_time + task_time

    for i in store:
        output.write(str(i))

    output.write("\n" + "Jack will work for " + str(jack_time) + " hours")
    output.write("\n" + "Jill will work for " + str(jill_time) + " hours")


file = open('input3.txt', 'r')
output = open('output3.txt', 'w')
n = int(file.readline())
time = [int(i) for i in file.readline().split()]
call = [i for i in file.readline()]
children(n, time, call)
