def quicksort(start,end,arr):
    p_i=start
    p=arr[p_i]
    while start<end:
        while start<len(arr) and arr[start]<=p:
            start+=1
        while arr[end]>p:
            end-=1
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
    arr[end],arr[p_i]=arr[p_i],arr[end]
    return end
def sorting(start,end,array):
    if start<end:
        p=quicksort(start,end,array)
        sorting(start,p-1,array)
        sorting(p+1,end,array)
a=[76,93,76,5,63,56,3,77,1,2,6]
print("Quick Sort")
sorting(0,len(a)-1,a)
print(f"{a}")


