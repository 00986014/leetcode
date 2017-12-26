def numIslands(self, grid):
    if not grid:
        return 0
    self.d = [[-1,0],[0,1],[1,0],[0,-1]]
    self.m, self.n = len(grid), len(grid[0])
    self.visited = []
    for i in range(self.m):
        self.visited.append([])
        for j in range(self.n):
            self.visited[-1].append(0)

    result = 0
    for i in range(self.m):
        for j in range(self.n):
            if grid[i][j] == '1' and self.visited[i][j] == 0:
                result += 1
                self.dfs(grid, i, j)
    return result
                
def dfs(self, grid, x, y):
    self.visited[x][y] = 1
    for i in range(4):
        newx = x + self.d[i][0]
        newy = y + self.d[i][1]
        if self.inArea(newx, newy) and self.visited[newx][newy] == 0 and\
           grid[newx][newy] == '1':
            self.dfs(grid, newx, newy)
    return
            


def inArea(self, x, y):
    return 0<=x<self.m and 0<=y<self.n
