def minion(arr,i,n):
     if i==n-1:
          return arr
     result = minion(arr,i+1,n)
     mario(result,i)
     return result
def mario(arr,i):
     if i==len(arr)-1:
          return
     if arr[i]>arr[i+1]:
          arr[i],arr[i+1] = arr[i+1],arr[i]
     mario(arr,i+1)
def recursive_bubble(lst):
     ans = minion(lst,0,len(lst))
     return ans
