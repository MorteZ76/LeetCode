# Dirty Coding, but it works. I will try to clean it up later.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix) 
        out = []
        if m == 0 :
            return out
        n = len(matrix[0])
        if m == 1 : 
            return matrix[0]
        if n == 1 :
            for i in range(m) :
                out.append(matrix[i][0])
            return out
        else  :
            i = 0 
            j = 0 
            while j < n :
                out.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
            while i < m :
                out.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            while j >= 0 :
                out.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            while i >0 :
                out.append(matrix[i][j])
                i -= 1
            sub_matrix = [row[1:n-1] for row in matrix[1:m-1]]
            if n== 2 or m == 2 :
                return out
            return out + self.spiralOrder(sub_matrix)
                

        