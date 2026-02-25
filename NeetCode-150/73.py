class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) 
        n = len(matrix[0])
        col = False 
        row = False 
        # bn = []
        # bm = []
        # for i in range(m) :
        #     bm.append(False)
        # for i in range(n) :
        #     bn.append(False)
        for i in range(m) :
            if matrix[i][0] == 0:
                col = True
        for j in range(n) :
            if matrix[0][j] == 0:
                row = True
        for i in range(1,m) :
            for j in range(1,n) :
                if matrix[i][j] == 0  :
                    # bm[i] = True
                    # bn[j] = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,m) :
            for j in range(1,n) :
                # if bm[i] == True or bn[j] == True  :
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        for i in range(m) :
            if col == True:
                matrix[i][0] = 0
        for j in range(n) :
            if row == True :
                matrix[0][j] = 0
        return matrix
        