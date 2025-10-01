def longestCommonSubsequence(text1, text2):
    n = len(text1)
    m = len(text2)
    dp = {}
    return solve(text1, text2, n, m, dp)

def solve(text1, text2, n, m, dp):
    if (n,m) in dp:
        return dp[(n,m)]
        
    if n==0 or m==0:
        return 0

    if n==1 and m==1:
        if text1 == text2:
            return 1

    if text1[n-1] == text2[m-1]:
        dp[(n,m)] = 1 + solve(text1, text2, n-1, m-1, dp)
        return dp[(n,m)]

    dp[(n,m)] = max(solve(text1, text2, n-1,m, dp),solve(text1, text2, n,m-1, dp))

    return dp[(n,m)]
