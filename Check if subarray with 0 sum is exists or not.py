def subarray(arr,n):
	 s=set()
	 sum=0
	 for i in range(n):
	 	sum += arr[i]
	 	if sum==0 or sum in s:
	 		return True
	 	s.add(sum)
	 return False 
arr=list(int(map,input().split()))
n=len(arr)
if subarray(arr,n)==True:
	print("True")
else:
	print("False")
