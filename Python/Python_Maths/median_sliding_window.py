n= int(input())  
arr = list(map(int, input().split())) 
k = int(input()) 

result = []

for i in range(n - k + 1):
    window = arr[i:i + k]
    window.sort()

    if k % 2 == 1:
        median = window[k // 2]
    else:
        median = (window[k // 2 - 1] + window[k // 2]) / 2
    result.append(float(median))

for median in result:
    print(median)
