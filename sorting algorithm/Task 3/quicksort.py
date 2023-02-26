def partition(Arr,p,r):
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
    return i
def Quick_sort(Arr,p,r):
    
    if p<r:
        q=partition(Arr,p,r)

        Quick_sort(Arr,p,q-1)
        Quick_sort(Arr,q+1,r)
    #return arr
    with open("output1.txt","w") as output:
        for i in Arr:
            output.write(str(i)+" ")
            
with open('input1.txt',"r") as file:
    temp = file.readlines()
arr = [int(a) for a in temp[1].strip("/n").split(" ")]
r= len(arr)-1
p=0

Quick_sort(arr,p,r)


