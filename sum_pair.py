def printPairs(arr, arr_size, sum):
	s = set()
	for i in range(0, arr_size): 
		temp = sum-arr[i] 
		if (temp in s): 
			print ("Pair with given sum " + str(sum) + " is (" + str(arr[i]) + ", " + str(temp) + ")")
		s.add(arr[i]) 

# driver program to check the above function 
A = list(map(int,input().split()))
n=int(input()) # sum
printPairs(A, len(A), n)
