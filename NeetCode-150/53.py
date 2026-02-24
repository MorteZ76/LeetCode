
# O(N), not optimmal
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        current_mx = nums[0]
        for i in range(1,len(nums)) :
            current_mx = current_mx + nums[i]
            if nums[i] > current_mx :
                current_mx = nums[i]
            if current_mx > mx :
                mx = current_mx
        return mx
            
        