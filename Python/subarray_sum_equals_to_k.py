def countSubarraysWithSumK(arr, k):
    # Your code goes here.
    num=0
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            if sum(arr[i:j+1])==k:
                num+=1
    return num
