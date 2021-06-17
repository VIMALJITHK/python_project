def addition(self, matrix1, matrix2):
    result = []
    if self.r1 == self.r2 & self.c1 == self.c2:
        for i in range(self.r1):
            sum = []
            for j in range(self.c2):
                s = self.matrix1[i][j] + self.matrix2[i][j]
                sum.append(s)
            result.append(sum)