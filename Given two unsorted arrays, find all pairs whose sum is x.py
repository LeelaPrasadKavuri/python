def findPairs(arr1, arr2, n, m, x):
    s = set() 
    for i in range (n): 
        s.add(arr1[i]) 
      
    for j in range(m): 
        if ((x - arr2[j]) in s): 
            print((x - arr2[j]), '', arr2[j]) 

print(" enter arr1 values")
arr1=list(map(int,input().split()))
print("enter arr2 values")
arr2=list(map(int,input().split()))
n=len(arr1)
m=len(arr2)
x=int(input())
finndpairs(arr1,arr2,n,m,x)
