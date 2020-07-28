def RotateMatrixClockwise(mat, N):    
    for i in range(0,int(N/2)):
        for j in range(i,N-1-i):
            temp = mat[i][j]
            mat[i][j] = mat[N-1-j][i]
            mat[N-1-j][i] = mat[N-1-i][N-1-j]
            mat[N-1-i][N-1-j] = mat[j][N-1-i]
            mat[j][N-1-i] = temp

    printMattrix(mat)
    print("\n")
    
def RotateMatrixAntiClkwise(mat, N):
    for i in range(0,int(N/2)):
        for j in range(i,N-1-i):
            temp = mat[i][j]
            mat[i][j] = mat[j][N-1-i]
            mat[j][N-1-i] = mat[N-1-i][N-1-j]
            mat[N-1-i][N-1-j] = mat[N-1-j][i]
            mat[N-1-j][i] = temp

    printMattrix(mat)
    print("\n")

def printMattrix(mat):
    for i in range(0,3):
        row = ""
        for j in range(0,3):            
            row = row + str(mat[i][j]) + " "
        print(row)        

matrix = [[1,2,3],[4,5,6],[7,8,9]]
printMattrix(matrix)

RotateMatrixClockwise(matrix, 3)
# RotateMatrixAntiClkwise(matrix, 3)