matrix = [[1, 14, 3],
          [4, 7, 6],
          [7, 8, 9]]

temp = 0
row = -1

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 7 == 0 and matrix[i][j] >= temp:
            temp = matrix[i][j]
            row = i
print(row)
