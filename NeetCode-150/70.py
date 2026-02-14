class Solution:
    def climbStairs(self, n: int) -> int:
        possible_moves = {}
        possible_moves[0] = 0
        possible_moves[1] = 1
        possible_moves[2] = 2
        i = 3
        while i <= n :
            possible_moves[i] = possible_moves[i-2] + possible_moves[i-1] 
            i += 1
        return possible_moves[n]
        