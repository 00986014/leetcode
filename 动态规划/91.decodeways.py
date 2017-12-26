def numDecodings(s):
    if not s:
        return 0
    if len(s) == 1:
        if s=='0':
            return 0
        else:
            return 1
        
    n = len(s)
    dp = [-1]*(n+1)
    dp[0], dp[1] = 0, 1
    
    if s[0]=='0' or s[1]=='0' and int(s[0])>2:
        return 0
    if int(s[:2])<=26 and int(s[:2])!=10 and int(s[:2])!=20:
        dp[2] = 2
    else:
        dp[2] = 1

    for i in xrange(3,n+1):
        if s[i-1]=='0':
            if s[i-2] == '1' or s[i-2] =='2':
                dp[i] = dp[i-2]
            else:
                return 0
        elif s[i-2]=='0':
            dp[i] = dp[i-1]
        elif int(s[i-2:i])>26:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1]+dp[i-2]

    return dp[n]

def numDecodings(s):
    if s == "":
        return 0
    dp = [0 for x in range(len(s)+1)]
    dp[0] = 1
    for i in range(1, len(s)+1):
        if s[i-1] != "0":
            dp[i] += dp[i-1]
        if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
            dp[i] += dp[i-2]
    return dp[len(s)]
