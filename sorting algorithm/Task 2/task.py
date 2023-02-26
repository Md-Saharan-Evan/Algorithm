
def combine(arr, LEFT_SUB, RIGHT_SUB):
    i = j = k = 0
    while i < len(LEFT_SUB) and j < len(RIGHT_SUB):
        if LEFT_SUB[i] < RIGHT_SUB[j]:
            arr[k] = LEFT_SUB[i]
            i += 1
        else:
            arr[k] = RIGHT_SUB[j]
            j += 1
        k += 1
    while i < len(LEFT_SUB):
        arr[k] = LEFT_SUB[i]
        i += 1
        k += 1
    while j < len(RIGHT_SUB):
        arr[k] = RIGHT_SUB[j]
        j += 1
        k += 1
    return arr
def merge_sort(arr):
    if len(arr) < 2:
        return
    mid = len(arr) // 2
    LEFT_SUB = arr[:mid]
    RIGHT_SUB = arr[mid:]
    merge_sort(LEFT_SUB)
    merge_sort(RIGHT_SUB)
    return combine(arr, LEFT_SUB, RIGHT_SUB)

    


with open('input.txt',"r") as file:
    temp = file.readlines()
arr = [int(x) for x in temp[1].strip("/n").split(" ")]


merge_sort(arr)
with open("output.txt","w") as output:
    
    for a in arr:
        output.write(str(a)+str(" "))
print(arr)