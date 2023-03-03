
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

#Expected:
# [[7,4,1],
#  [8,5,2],
#  [9,6,3]]

#Process for rotating a matrix
#1. transpose all elements
#2. reverse all elements

def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix[0])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    return matrix


def reverse(matrix):
    for i in range(len(matrix)):
        left = 0
        right = len(matrix[0])-1
        while left<right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left+=1
            right-=1
    return matrix

print(matrix)
transpose(matrix)
reverse(matrix)
print(matrix)