class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1 :
            return 1
        mx = max(m-1,n-1)
        mn = min(m-1,n-1)
        final_res =1 
        i = mx + mn
        while i > mx :
            final_res = i * final_res 
            i -= 1
        while mn > 0 :
            final_res = final_res // mn
            mn -= 1
        return final_res
        