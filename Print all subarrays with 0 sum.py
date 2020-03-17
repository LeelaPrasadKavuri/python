def subarray(arr,n):
	hashmap={}
	out=[]
	sum1=0
	for i in range(n):
		sum1+=arr[i]
		if sum1==0:
			out.append((0,i))
		al=[]
		if sum1 in hashmap:
			al=hashmap.get(sum1):
			for it in range(len(al)):
				out.append((al[it]+1,i))
		al.append(i)
		hashmap[sum1]=al
	return out
def printouput(output):
	for i in output:
		print( " Subarray index" + str(i[0])+"to"+str(i[1]))
arr=list(map(int,input().split()))
n=len(arr)
out=subarray(arr,n)
if (len(out)==0):
	print("subarray does not exist")
else:
	printouput(out)
		
