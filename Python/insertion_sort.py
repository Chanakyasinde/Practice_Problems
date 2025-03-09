def outer(lst,i):
     if i==len(lst):
          return 
     inner(lst,i-1,lst[i])
     outer(lst,i+1)

def inner(lst,j,k):
     if j<0 or lst[j]<=k:
          lst[j+1]=k
          return 
     lst[j+1]=lst[j]
     inner(lst,j-1,k)

def recursive_insertion(lst):
     outer(lst,0)
     return lst
