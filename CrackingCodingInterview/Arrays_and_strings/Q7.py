def NullifyRow(matrix, rowNo):
    for j in range(0,len(matrix[0])):
        matrix[rowNo][j] = 0

def NullifyCol(matrix, colNo):
    for i in range(0,len(matrix)):
        matrix[i][colNo] = 0
        
def SetZeroes(matrix):
    rowHasZero = False
    colHasZero = False

    # Check i first row has zero 
    for j in range(0,len(matrix[0])):
        if(matrix[0][j] == 0):
            rowHasZero = True
            break

    # Check if first column has zero
    for i in range(0,len(matrix)):
        if(matrix[i][0] == 0):
            colHasZero = True
            break

    # Change origin points to zero if any element in 0
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if(matrix[i][j] == 0):
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Based on whether origin is zero, change all elements of row to 0
    for i in range(1,len(matrix)):
        if(matrix[i][0] == 0):
            NullifyRow(matrix, i)

    # Based on whether origin is zero, change all elements of column to 0
    for j in range(1,len(matrix[0])):
        if(matrix[0][j] == 0):
            NullifyCol(matrix, j)
    
    if(rowHasZero):
        NullifyRow(matrix, 0)
    if(colHasZero):
        NullifyCol(matrix, 0)

    print(matrix)



matrix = [[ 1, 1, 0, 1, 1 ],
		  [ 1, 1, 1, 1, 1 ],
		  [ 1, 1, 0, 1, 1 ],
		  [ 1, 1, 1, 1, 1 ],
		  [ 0, 1, 1, 1, 1 ]]

SetZeroes(matrix)