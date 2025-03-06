target = int(input())
nums = list(map(int, input().split()))

n = len(nums)
left = 0
sum = 0
minLength = float('inf')

for right in range(n):
    sum += nums[right]
    
    while sum >= target:
        minLength = min(minLength, right - left + 1)
        sum -= nums[left]
        left += 1

if minLength == float('inf'):
    print(0)
else:
    print(minLength)
