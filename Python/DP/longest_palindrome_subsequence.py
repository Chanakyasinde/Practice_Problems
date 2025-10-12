def longestPalindromeSubseq(s):
    n=0
    m=len(s)-1
    dp = {}
    return solve(s, n, m, dp)

def solve(s, n, m, dp):
    if (n,m) in dp:
        return dp[(n,m)]
    if n > m:
        return 0
    if n==m:
        return 1
    if s[n] == s[m]:
        dp[(n,m)] = 2 + solve(s,n+1,m-1,dp)
        return dp[(n,m)]
    dp[(n,m)] = max(solve(s,n+1,m,dp),solve(s,n,m-1,dp))

    return dp[(n,m)]
