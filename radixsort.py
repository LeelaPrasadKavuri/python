def countingsort(arr,exp1):
    n=len(arr)
    output=[0]*(n)
    count=[0]*(10)
    for i in range(0,n):
        index=(arr[i]/exp1)
        count[(index)%10]+=1
    for i in range(1,10):
        count[i]