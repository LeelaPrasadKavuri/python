import math
def jumpsearch (arr,x ,n):
    step=math.sqrt(n)
    prev=0
    while arr[int(min(step,n)-1)] < x:
        prev=step
        step+=math.sqrt(n)
        if prev >= n:
            return -1
    while arr[int(prev)]<x:
        prev+=1
        if prev==min(step,n):
            return -1
    if arr[int(prev)]==x:
        return prev
    return -1
print("enter elements") 
arr=list(map(int,input().split()))
x=int(input())
n=len(arr)
 
index = jumpsearch(arr, x, n)  
print("Number" , x, "is at index" ,"%.0f"%index) 
  