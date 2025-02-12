def recurse(nums, i):
    # base case
    if i>=len(nums):
        return 0
    # recursive case
    ans_i_1 = recurse(nums,i+1)
    ans_i_2 = recurse(nums,i+2)
    chori = nums[i]+ans_i_2
    chori_nah = 0 + ans_i_1
    return max(chori, chori_nah)

def rob(nums):
    return recurse(nums,0)
