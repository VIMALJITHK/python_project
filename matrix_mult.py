
r1 = int(input('enter num of row of matrix1: '))
c1 = int(input('enter num of colm of matrix1: '))
c2 = int(input('enter the num of colm of matrix2: '))

print('enter the values for matrix1: ')
matrix1 = [[int(input()) for i in range(c1)] for j in range(r1)]
print(matrix1)

print('enter the values for matrix2: ')
matrix2 = [[int(input()) for i in range(c2)] for j in range(c1)]
print(matrix2)

result = [[0 for i in range(c2)] for j in range(r1)]

for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
print(result)