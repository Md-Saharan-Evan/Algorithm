with open("input1.txt","r") as file:
    T=int(file.readline())
    arr=file.readline().split(" ")
    new=[]
## here in this code, we are using nasted for loop to sort the array
## we know each nasted loop will run n*n times and the order of the function would be O(n^2)
## if the array is sorted then no need to enter in function and the order would be O(n)  
    for a in range(T-1):
        if arr[a]<=arr[a+1]:
            new.append(arr[a])
    new.append(arr[T-1])
    if new==arr:
        print("already sorted")
    else:
        def bubbleSort(arr):  #n+1 times
            for i in range(T): #n times 
                for j in range(T-1): # n*n times
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
        
    
        bubbleSort(arr)
    with open("output1.txt","w") as output:
        for val in arr:
            output.write(val+" ")