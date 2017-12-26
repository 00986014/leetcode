def uniquePaths(m, n):
    if m<=0 or n<=0:
        return 0

    grid = []
    for i in xrange(m):
        grid.append([])
        for j in xrange(n):
            grid[-1].append(0)

    for i in xrange(n):
        grid[0][i] = 1
    for j in xrange(m):
        grid[j][0] = 1

    for i in xrange(1, m):
        for j in xrange(1, n):
            grid[i][j] = grid[i-1][j]+grid[i][j-1]

    return grid[-1][-1]
        
