def rob(nums):
    dp = {}
    return solve(0, nums, dp)

def solve(index, nums, dp):
    if index >= len(nums):
        return 0
    if index in dp:
        return dp[index]
    take = nums[index] + solve(index+2, nums, dp)
    not_take = solve(index+1, nums, dp)
    dp[index] = max(take, not_take)
    return dp[index]
