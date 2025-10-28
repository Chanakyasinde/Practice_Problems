def LIS_ending_at_ith_index(dp, A, i):
    if i == 0:
        return 1
    if i in dp:
        return dp[i]
    answer = 1
    for j in range (i):
        if (A[j] < A[i]):
            answer = max(answer, 1+LIS_ending_at_ith_index(dp, A, j))
    dp[i] = answer
    return dp[i]

def lengthOfLIS(nums):
    answer = 1
    dp = {}
    for i in range(len(nums)):
        answer = max(answer, LIS_ending_at_ith_index(dp, nums, i))
    return answer

# 2nd approach

def lengthOfLIS(nums):
    n = len(nums)
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
