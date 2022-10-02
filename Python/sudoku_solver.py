import time
def findNextCellToFill(grid, i, j):
    for x in range(i,9):
        for y in range(j,9):
            if grid[x][y]==0:
                return x,y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1,-1
def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX,secTopY=3*(i//3),3*(j//3)  # floored quotient should be used here.
            for x in range(secTopX,secTopX+3):
                for y in range(secTopY,secTopY+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False
def solveSudoku(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
                grid[i][j] = 0
    return False
a=[[4,0,9,0,0,8,0,3,0],[7,5,0,0,3,2,0,1,8],[0,0,0,5,0,0,2,0,6],[8,0,0,0,0,3,9,0,0],[0,3,0,0,4,0,0,7,5],
           [0,0,1,2,0,7,0,0,0],[0,0,8,4,0,0,0,0,9],[0,1,0,0,0,9,0,4,0],[2,0,0,7,1,0,8,5,0]]
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

print_board(a)
print("________________________________")
t1=time.time()
solveSudoku(a)
print_board(a)
print(time.time()-t1)
