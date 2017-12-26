def coinChange(coins, amount):
    if not coins:
        return -1

    l = [-1]*(amount+1)
    l[0] = 0


    for i in xrange(amount+1):
        for j in coins:
            if j>amount:
                continue
            if l[i-j] != -1:
                if l[i] == -1:
                    l[i] = l[i-j]+1
                else:
                    l[i] = min(l[i], l[i-j]+1)

    return l[amount]


