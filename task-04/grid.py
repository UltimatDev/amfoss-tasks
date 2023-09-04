result=""
checklist=["XXX","+++","OOO"]
def checkdraw():
    global result
    if result=="":
       return True
    else:
    
        result="Draw"
        return False    

def horizontal(grid):
    global result
    for line in grid:
        
        if line in checklist:
            if checkdraw():
                result=line[0]

def diag(grid):
    global result
    
    if grid[0][0]+grid[1][1]+grid[2][2] in checklist:
        if checkdraw():
            result = grid[0][0]

    if grid[0][2]+grid[1][1]+grid[2][0] in checklist:
        if checkdraw():
            result = grid[0][2]

def vertical(grid):
    global result
    for x in range(3):
        if grid[0][x]+grid[1][x]+grid[2][x] in checklist:
            
            if checkdraw():
        
                result = grid[0][x]


charl=['X','+','O']

test_cases=int(input())
grids=[]#Main list of grids
for x in range(test_cases):
    grid=[]#temp sub list variable to store grid
    for x in range(3):
        row=input("")
        grid.append(row)
    grids.append(grid)
print(grids)

for grid in grids:
    result=""
    horizontal(grid)
    diag(grid)
    vertical(grid)
    if result !="":
        print(result)
    else:
        print("Draw")
