def fill_matrix(matrix, block):
    counter = 4
    for i in range(0,len(block),counter):
        index = i // counter
        column = index // 4
        row = index % 4
        matrix[row][column] = block[i:i+4]
    return matrix

