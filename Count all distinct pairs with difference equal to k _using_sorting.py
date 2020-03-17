def binarySearch(arr, low, high, x):
	if (high >= low):	
		mid = low + (high - low)//2
		if x == arr[mid]: 
			return (mid) 
		elif(x > arr[mid]): 
			return binarySearch(arr, (mid + 1), high, x) 
		else: 
			return binarySearch(arr, low, (mid -1), x)	
	return -1
 
def countPairsWithDiffK(arr, n, k):
	count = 0
	arr.sort()	 
	for i in range (0, n - 2): 
		if (binarySearch(arr, i + 1, n - 1, 
						arr[i] + k) != -1): 
			count += 1
	return count 

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print ("Count of pairs with given diff is ", 
			countPairsWithDiffK(arr, n, k)) 


	
