def partition(Arr,p,r,key):
    pivot=Arr[p]
    i=p
    j=i+1
    while j <=r:
        if pivot<=Arr[j]:
            j+=1
        else:
            i+=1
            Arr[i],Arr[j]=Arr[j],Arr[i]
            j+=1
    Arr[i],Arr[p]=Arr[p],Arr[i]
    
    if key==i:
        print(Arr[i])
    elif key<i:
        r=i-1
        partition(Arr,p,r,key)
    else:
        p=i+1
        partition(Arr,p,r,key)
    
arr=[1,3,4,5,9,10,10]
p=0
r=len(arr)-1
key=5-1
partition(arr,p,r,key)