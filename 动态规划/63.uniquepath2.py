def uniquePaths(obstacleGrid):
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0

    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    for i in xrange(m):
        if obstacleGrid[i][0] == 1:
            for k in xrange(i, m):
                obstacleGrid[k][0] = 0
            break
        else:
            obstacleGrid[i][0] = 1

    for j in xrange(1, n):
        if obstacleGrid[0][j] == 1:
            for k in xrange(j, n):
                obstacleGrid[0][k] = 0
            break
        else:
            obstacleGrid[0][j] = 1

    for i in xrange(1, m):
        for j in xrange(1, n):
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
            else:
                obstacleGrid[i][j] = obstacleGrid[i-1][j]+obstacleGrid[i][j-1]

    return obstacleGrid[-1][-1]
    
