# python program to find length of the largest 
# subarray which has all contiguous elements */ 

# This function prints all distinct elements 
def findLenght(arr, n): 
	max_len = 1
	for i in range(0,n - 1): 

		# Create an empty hash set and 
		# add i'th element to it 
		myset = set() 
		myset.add(arr[i]) 

		# Initialize max and min in 
		# current subarray 
		mn = arr[i] 
		mx = arr[i] 
		for j in range(i + 1,n): 

			# If current element is already 
			# in hash set, then this subarray 
			# cannot contain contiguous elements 
			if arr[j] in myset: 
				break


			# Else add current element to hash 
			# set and update min, max if required. 
			myset.add(arr[j]) 
			mn = min(mn, arr[j]) 
			mx = max(mx, arr[j]) 

			# We have already checked for 
			# duplicates, now check for other 
			#property and update max_len 
			# if needed 
			if mx - mn == j - i: 
				max_len = max(max_len, mx - mn + 1) 

	return max_len # Return result 


# Driver code 

arr = [10, 12, 12, 10, 10, 11, 10] 
n = len(arr) 
print("Length of the longest contiguous subarray is", 
								findLenght(arr,n)) 



