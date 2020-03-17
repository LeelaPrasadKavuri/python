def printpairs(arr,arr_size,n):
	s=set()
	for i in range(arr_size):
		temp=n-arr[i]
		if (temp in s):
			print("Pair with given sum "+ str(n) + " is (" + str(arr[i]) + ", " + str(temp) + ")")
		s.add(arr[i])

a=list(map(int,input().split()))
n=16
printpairs (a,len(a),n)


