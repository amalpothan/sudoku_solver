grid=[[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

def checkValid(grid,num,pos):
    #check row
    for j in range(len(grid[0])):
        if grid[pos[0]][j]==num and pos[1]!=j:
            return False
    #check column
    for i in range(len(grid)):
        if grid[i][pos[1]]==num and pos[0]!=i:
            return False
    x_box=pos[0]//3
    y_box=pos[1]//3
    #check box
    for i in range(x_box*3,(x_box*3)+3):
        for j in range(y_box * 3, (y_box * 3) + 3):
            if grid[i][j]==num and pos!=(i,j):
                return False
    return True

def solve(grid):
    empty=nextEmpty(grid)
    if not empty:
        return True
    else:
        row,col=empty
    for i in range(1,10):
        if checkValid(grid,i,empty):
            grid[row][col]=i
            if solve(grid):
                return True
            grid[row][col] = 0
    return False


def print_puzzle(grid):
    for i in range(len(grid)):
        if i%3==0 and i>0:
            print('----------------------')
        for j in range(len(grid[0])):
            if j%3==0 and j>0:
                print("|", end=" ")

            if j<8:
                print(grid[i][j],end=" ")
            else:
                print(grid[i][j])

def nextEmpty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                return (i,j)
    return None

print_puzzle(grid)
solve(grid)
print("\n")
print_puzzle(grid)
