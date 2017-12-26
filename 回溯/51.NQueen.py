# coding:utf8
def solveNQueens(self, n):
    self.result = []
    self.col, self.dia1, self.dia2 = [], [], []
    for i in range(n):
        self.col.append(0)

    for i in range(2*n-1):
        self.dia1.append(0)
        self.dia2.append(0)

    row = []
    self.putQueen(n, 0, row)
    return self.result

# 尝试在n皇后问题中摆放第index行的皇后位置 
def putQueen(self, n, index, row):
    if index == n:
        self.result.append(self.generateBoard(n, row))
        return

    for i in range(n):
        # 尝试将第index行的皇后摆放在第i列
        if (self.col[i]==0 and self.dia1[index+i]==0 and \
            self.dia2[index-i+n-1]==0):
            row.append(i)
            self.col[i] = 1
            self.dia1[index+i] = 1
            self.dia2[index-i+n-1] = 1
            self.putQueen(n, index+1, row)
            self.col[i] = 0
            self.dia1[index+i] = 0
            self.dia2[index-i+n-1] = 0
            row.pop()

    return

def generateBoard(self, n, row):
    board = []
    for i in range(n):
        board.append('')
        for j in range(n):
            if j == row[i]:
                board[-1]+='Q'
            else:
                board[-1]+='.'
    return board
