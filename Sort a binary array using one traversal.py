# A Python program to sort a 
# binary array 
def sortBinaryArray(a, n): 
	j = -1
	for i in range(n): 

		# if number is smaller 
		# than 1 then swap it 
		# with j-th number 
		if a[i] < 1: 
			j = j + 1
			
			# swap 
			a[i], a[j] = a[j], a[i] 
	

# Driver program 
a = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 
		1, 1, 0, 0, 1, 1, 0, 1, 0, 0] 
n = len(a) 

sortBinaryArray(a, n) 

for i in range(n): 
		print(a[i], end = " ") 

# This code is contributed by Shrikant13. 

