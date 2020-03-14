def rverseArray(arr, start, end): 
    while (start < end): 
        temp = arr[start] 
        arr[start] = arr[end] 
        arr[end] = temp 
        start += 1
        end = end-1
  
def leftrotate(arr,d,n): 
  
    if d == 0: 
        return
    rverseArray(arr, 0, d-1) 
    rverseArray(arr, d, n-1) 
    rverseArray(arr, 0, n-1) 


n=int(input())
d=int(input())
arr=list(map(int,input().split()))
leftrotate(arr,d,n)
print(arr)
