def numSquares(n):
    dp = [-1] * (n + 1)
    dp[0] = 0

    for i in xrange(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = dp[i - j * j]  + 1 if dp[i] == -1 else\
                    min(dp[i - j * j]  + 1, dp[i])
            j += 1
    return dp[n]


