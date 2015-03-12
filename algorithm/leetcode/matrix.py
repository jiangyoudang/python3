class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    res = []
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0: return self.res
        n = len(matrix[0])
        if n==0: return self.res

        for i in matrix[0]:
            self.res.append(i)
        for i in range(1,m):
            self.res.append(matrix[i][-1])
        if m>1 and n>1:
            for i in matrix[-1][n-2::-1]:
                self.res.append(i)
            for i in range(m-2, 0, -1):
                self.res.append(matrix[i][0])
            matrix_new = []
            for row in matrix[1:-1]:
                matrix_new.append(row[1:-1])
            self.spiralOrder(matrix_new)
        return self.res

    def spiralOrder2(self, matrix):
        res = []
        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            self.spiral(matrix, 0, m-1, 0, n-1, res)
        return res

    def spiral(self, matrix, i1, i2, j1, j2, res):
        if i1>i2 or j1>j2: return
        for col_i in range(j1,j2+1):
            res.append(matrix[i1][col_i])
        for row_i in range(i1+1, i2+1):
            res.append(matrix[row_i][j2])
        if i1 < i2 and j1< j2:
            for col_i in range(j2-1,j1-1,-1):
                res.append(matrix[i2][col_i])
            for row_i in range(i2-1, i1,-1):
                res.append(matrix[row_i][j1])
        self.spiral(matrix, i1+1,i2-1,j1+1,j2-1,res)


    def generateMatrix(self, n):
        count = 1
        matrix = [[1] *n for i in range(n)]
        i1, i2, j1, j2 = 0, n-1, 0, n-1
        while i1<=i2 and j1<=j2:
            for col_i in range(j1,j2+1):
                matrix[i1][col_i] = count
                count += 1
            for row_i in range(i1+1, i2+1):
                matrix[row_i][j2] = count
                count += 1
            if i1 < i2 and j1< j2:
                for col_i in range(j2-1,j1-1,-1):
                    matrix[i2][col_i] = count
                    count += 1
                for row_i in range(i2-1, i1,-1):
                    matrix[row_i][j1] = count
                    count += 1
            i1, i2, j1, j2 = i1+1, i2-1, j1+1, j2-1
        return matrix

res = Solution().generateMatrix(5)
print(res)