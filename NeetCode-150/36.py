class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check :
        for row in board :
            numbers = set() 
            for num in row :
                if num != "." :
                    if num in numbers :
                        return False 
                    else :
                        numbers.add(num)

        # column check:
        for col in range(len(board))  :
            numbers = set()
            for row in board :
                num = row[col] 
                if num != "." :
                    if num in numbers :
                        return False 
                    else :
                        numbers.add(num)

        # 3 by 3 check :
        for i in range(3) :
            for j in range(3) : 
                numbers = set() 
                for k in range(3) :
                    for l in range(3) :
                        num = board[i *3 + k][j*3 + l]
                        if num != "." :
                            if num in numbers :
                                return False 
                            else :
                                numbers.add(num)
        return True


        