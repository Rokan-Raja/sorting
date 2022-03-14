def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
a=[6,7,9,2,7,12,3,98,87]
bubblesort(a)
print('Bubble Sort')
for i in range(len(a)):
    print(a[i],end=",")

