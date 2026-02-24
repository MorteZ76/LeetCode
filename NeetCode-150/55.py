class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = nums[0]
        if len(nums) == 1 :
            return True
        near = 1 
        while near <= furthest :
            furthest = max(furthest, near + nums[near])
            if furthest >= len(nums)-1 :
                return True
            near += 1
        return False
        