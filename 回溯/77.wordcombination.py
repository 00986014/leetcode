#coding:utf8
def exist(board, word):
    d = [[-1,0],[0,1],[1,0],[0,-1]]
    m, n = len(board), len(board[0])
    visited = []
    for i in range(m):
        visited.append([])
        for j in range(n):
            visited[-1].append(0)
            
            
    for i in xrange(len(borad)):
        for j in xrange(len(board[i])):
            if searchWord(board, word, i, j):
                return True
    return False

#从board[startx][starty]开始寻找word
def searchWord(board, word, startx, starty):
    if len(word) == 1:
        return board[startx][starty] == word[0]

    if board[startx][starty] == word[0]:
        visited[startx][starty] = 1
        for i in range(4):
            newx = startx + d[i][0]
            newy = starty + d[i][1]
            if inArea(newx, newy) and visited[newx][newy] == 0:
                if searchWord(board, word[1:], newx, newy):
                    return True
        visited[startx][starty] = 0

    return False


def inArea(x, y):
    return 0<=x<m and 0<=y<n
