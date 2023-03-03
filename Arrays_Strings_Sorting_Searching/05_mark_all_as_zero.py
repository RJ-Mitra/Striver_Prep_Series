#given a matrix, if a zero is encountered, mark all values in its row and col as 0

input = [[1,1,1],
         [1,0,1],
         [1,1,1],
         [1,1,1]]

def setCols0(input, r):
    for i in range(len(input[0])):
        input[r][i] = 0
    return input

def setRows0(input, c):
    for i in range(len(input)):
        input[i][c] = 0
    return input

row_arr = [ -1 for i in input]
col_arr = [ -1 for i in input[0]]

for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 0:
            row_arr[j] = 0
            col_arr[i] = 0

for i in range(len(row_arr)):
    if row_arr[i] == 0:
        input = setCols0(input,i)

for j in range(len(col_arr)):
    if col_arr[j] == 0:
        input = setRows0(input,j)


print(input)