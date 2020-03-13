def binary(arr,l,r,x):
    if r >=l:
        mid =l +(r-l)//2
        if arr[mid]==x:
            return mid
        if arr[mid] > x:
            return binary(arr,l,mid-1,x)
        return binary(arr,mid+1,r,x)
    return -1
def expo(arr,n,x):
    if arr[0]==x:
        return 0
    i=1
    while i<n and arr[i] <= x:
        i=i*2
    return binary(arr,i//2,min(i,n),x)
arr=list(map(int,input().split()))
n=len(arr)
x=int(input())
print(expo(arr,n,x))
