# Python3 program to print subarray with sum as given sum 

# Function to print subarray with sum as given sum 
def subArraySum(arr, n, Sum): 

	# create an empty map 
	Map = {} 
	
	# Maintains sum of elements so far 
	curr_sum = 0
	
	for i in range(0,n): 
	
		# add current element to curr_sum 
		curr_sum = curr_sum + arr[i] 
	
		# if curr_sum is equal to target sum 
		# we found a subarray starting from index 0 
		# and ending at index i 
		if curr_sum == Sum: 
		
			print("Sum found between indexes 0 to", i) 
			return
		
	
		# If curr_sum - sum already exists in map 
		# we have found a subarray with target sum 
		if (curr_sum - Sum) in Map: 
		
			print("Sum found between indexes", \ 
				Map[curr_sum - Sum] + 1, "to", i) 
			
			return
	
		Map[curr_sum] = i 
	
	# If we reach here, then no subarray exists 
	print("No subarray with given sum exists") 

	
# Driver program to test above function 
if __name__ == "__main__": 

	arr = list(map(int,input().split()))
	n = len(arr) 
	Sum = int(input())
	
	subArraySum(arr, n, Sum) 
	
 

