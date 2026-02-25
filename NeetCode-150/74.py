class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_matrix = []
        for i in matrix: 
            col_matrix.append(i[0])
        row = self.binary_search(col_matrix, target)
        if row == -1 :
            return False 
        col = self.binary_search(matrix[row],target) 
        if matrix[row][col] == target :
            return True
        return False




    def binary_search(self,nums, val) :
                start = 0 
                end = len(nums)- 1
                if (nums[start] > val) :
                    return -1
                while (end > start + 1) :
                    mid = (end + start ) // 2
                    if ( nums[mid] > val ) :
                        end = mid -1 
                    elif ( nums[mid] == val ) :
                         return mid
                    else :
                        start = mid
                if ( nums[end] <= val ) :
                        return end
                elif ( nums[start] <= val ) :
                        return start
                else :
                    return start -1
