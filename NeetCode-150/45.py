# Not optimal solution : 
class Solution:
    def jump(self, nums: List[int]) -> int:
        i = len(nums) - 1 
        dp = {}
        for j in range(1000) :
            dp[i+j] = 0
        i -= 1 
        while i >= 0 :
            mn = 100000000
            for j in range(nums[i]) :
                if dp[i+j +1] + 1 < mn :
                    mn =  dp[i+j +1] + 1   
            dp [i] = mn 
            i -= 1

        return dp[0]
        