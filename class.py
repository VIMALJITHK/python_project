
class Matrices:
    def readMatrix(self, r, c):
        '''
        This function is to read matrix
        parameters:
        argument1 (int): num of rows of matrix
        argument2 (int): num of colms of matrix

        retuns:
        list: matrix

        '''

        matrix = [[int(input()) for i in range(c)] for j in range(r)]

        return matrix

    def add(self, r, c):
        print('enter the elements for matrix1: ')
        m1 = self.readMatrix(r, c)

        print('enter the elements for matrix2: ')
        m2 = self.readMatrix(r, c)

        sumResult = []
        for i in range(r):
            sum = []
            for j in range(c):
                s = m1[i][j] + m2[i][j]
                sum.append(s)
            sumResult.append(sum)

        return sumResult

    def mult(self, r1, c1, c2):
        print('enter the elements for matrix1: ')
        m1 = self.readMatrix(r1, c1)

        print('enter the elements for matrix2: ')
        m2 = self.readMatrix(c1, c2)

        result = [[0 for i in range(c2)] for j in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    result[i][j] += m1[i][k] * m2[k][j]

        return result

    def printMatrix(self, m):
        for i in range(len(m)):
            for j in range(len(m[0])):
                print(format(m[i][j], "<5"), end='')
            print()

    def menu(self, k):



mat = Matrices()
condition = True

while condition:
    k = int(input('enter 0 for add and 1 for mult: '))

    if k == 0:
        print('addition')
        r = int(input('enter num of rows of m1: '))
        c = int(input('enter num of colms of m2: '))

        sumResult = mat.menu(k)
        mat.printMatrix(sumResult)

    elif k == 1:
        print('multiplication')
        r1 = int(input('enter num of rows of m1: '))
        c1 = int(input('enter num of colms of m1: '))
        c2 = int(input('enter  num of colms of m2: '))

        multResult = mat.menu(k)
        mat.printMatrix(multResult)

    else:
        condition = False
        print('exit')















