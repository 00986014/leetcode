def minPathSum(grid):
    if not grid:
        return
    for i in xrange(1, len(grid[0])):
        grid[0][i] += grid[0][i-1]
    for j in xrange(1, len(grid)):
        grid[j][0] += grid[j-1][0]

    for i in xrange(1, len(grid)):
        for j in xrange(1, len(grid[0])):
            grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]

    return grid[-1][-1]
