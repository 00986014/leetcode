def findMaxForm(strs, m, n):
    if not m and not n:
        return 0

    dp = [[0] * (n + 1) for _ in xrange(m + 1)]

    for string in strs:
        zeros, ones = string.count('0'), string.count('1')
        for z in range(m, zeros - 1, -1):
            for o in range(n, ones - 1, -1):
                dp[z][o] = max(dp[z][o], dp[z - zeros][o - ones] + 1)

    return dp[m][n]
