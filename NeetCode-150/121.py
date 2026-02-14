class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = 0
        min_for_now = 100000
        max_for_now = -1
        i = 0 
        while i < len(prices) :
            if prices[i] < min_for_now :
                min_for_now = max_for_now = prices[i] 
            if prices[i] > max_for_now :
                max_for_now = prices[i] 
                max_so_far = max (max_so_far, max_for_now - min_for_now) 

            i += 1
        return max_so_far
        