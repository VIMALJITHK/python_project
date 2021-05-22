matrix1 = []
r = int(input('enter num of rows: '))
c = int(input('enter num of column: '))

print('enter the element: ')
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    matrix1.append(row)
print(matrix1)
print('matrix1 is: ')
for i in range(r):
    for j in range(c):
        print(format(matrix1[i][j],"<5"),end='')
    print()

matrix2 = []
print('enter the matrix2 element2: ')
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    matrix2.append(row)
print(matrix2)
print('matrix2 is: ')
for i in range(r):
    for j in range(c):
        print(format(matrix2[i][j],"<5"), end = '')
    print()

result=[]
for i in range(r):
    sum = []
    for j in range(c):
        s = matrix1[i][j] + matrix2[i][j]
        sum.append(s)
    result.append(sum)
print('resultand matrix is: ')
for i in range(r):
    for j in range(c):
        print(format(result[i][j], "<5"), end='')
    print()