
def zeroColumn(matrix, colIdx):
    n = len(matrix)
    for i in range(n):
        matrix[i][colIdx] = 0
    return matrix

def zeroRow(matrix, rowIdx):
    n = len(matrix)
    for i in range(n):
        matrix[rowIdx][i] = 0
    return matrix

# O(n^2) time, O(1) space
def zeroMatrix(matrix):
    indices = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                indices.append((i,j))

    # Have to do this later, otherwise we mess up previous values
    for i, j in indices:
        matrix = zeroRow(matrix, i)
        matrix = zeroColumn(matrix, j)
    return matrix

matrix = [[1, 2, 3],[4, 0, 6],[7, 8, 9]]
result = zeroMatrix(matrix)
print(result)

matrix = [[0, 1, 2, 3],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]]
result = zeroMatrix(matrix)
print(result)
