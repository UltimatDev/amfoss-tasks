def horizontal(line):
    pass


test_cases=int(input("Enter Number of test cases"))
grids=[]#Main list of grids
for x in range(test_cases):
    grid=[]#temp sub list variable to store grid
    for x in range(3):
        row=input("")
        grid.append(row)
    grids.append(grid)
print(grids)
