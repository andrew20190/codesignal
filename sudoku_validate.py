import numpy as np

def validate_sodoku(data):
    
    required = list(range(1,10))
    
    for req in range(1,10):
        if data.count(req) != 1:
            print('Failed', req)
            return False
    
    return True

def sudoku(grid_list):
    grid = np.array(grid_list)
    
    for rowidx in range(0, len(grid_list)):
        rowdata = grid[rowidx, 0 : len(grid_list)]
        print('row', rowidx, rowdata)
        if validate_sodoku(rowdata.tolist()) == False:
            return False
        
    for colidx in range(0, len(grid_list[0])):
        coldata = grid[0 : len(grid_list[0]), colidx]
        print('col', colidx, coldata)
        if validate_sodoku(coldata.tolist()) == False:
            return False
    
    # check the subgrids too, at 
    # (0,0), (0,3), (0,6)
    # (3,0), (3,3), (3,6)
    # (6,0), (6,3), (6,6)
    for top in [0,3,6]:
        for left in [0,3,6]:
            subgrid = grid[top:top+3, left:left+3]
            flat_list = sum(subgrid.tolist(), [])
            if validate_sodoku(flat_list) == False:
                return False
    
    return True

#sudoku(grid)
