
class Matrices:

    def operation(self):
        '''

        This function takes an option from user and perform the matrix operation

        '''

        while True:
            option = input('''
            
                1: Addition
                2: Multiplication

                make a selection from 1, 2:
                            ''')

            if option == "1":
                print('addition')
                r = int(input('enter num of rows of m1: '))
                c = int(input('enter num of colms of m2: '))

                sumResult = mat.add(r, c)
                mat.printMatrix(sumResult)

            elif option == "2":
                print('multiplication')
                r1 = int(input('enter num of rows of m1: '))
                c1 = int(input('enter num of colms of m1: '))
                c2 = int(input('enter  num of colms of m2: '))

                multResult = mat.mult(r1, c1, c2)
                mat.printMatrix(multResult)

            else:
                print('exit')
                break

    def readMatrix(self, r, c):
        '''

        This function is to read matrix
        parameters:
        argument1 (int): num of rows of matrix
        argument2 (int): num of colms of matrix

        return:
        list: matrix

        '''

        matrix = [[int(input()) for i in range(c)] for j in range(r)]

        return matrix

    def add(self, r, c):
        '''

        This function do the addition

        :param r:Number of rows of matrix1
        :param c: Number of columns of matrix2

        :return:
        List: Summation

        '''
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
        '''

        This function do multiplication

        :param r1: Number of rows of matrix1
        :param c1: Number of columns of matrix1
        :param c2: Number of columns of matrix2

        :return:
         List: Multiplication

        '''
        print('enter the elements for matrix1: ')
        m1 = self.readMatrix(r1, c1)

        print('enter the elements for matrix2: ')
        m2 = self.readMatrix(c1, c2)

        multResult = [[0 for i in range(c2)] for j in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    multResult[i][j] += m1[i][k] * m2[k][j]

        return multResult

    def printMatrix(self, m):
        '''

        This function will print the result summation/multiplication in matrix form

        :param m: Resultant matrix from summation/multiplication\

        '''
        for i in range(len(m)):
            for j in range(len(m[0])):
                print(format(m[i][j], "<5"), end='')
            print()

mat = Matrices()
mat.operation()


















