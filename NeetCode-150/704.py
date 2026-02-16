class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle_index = int (len(nums)/2)
        if len (nums) == 0 :
            return -1 
        if nums[middle_index] == target :
            return middle_index
        if nums[middle_index] > target :
            return self.search(nums[:middle_index], target) 
        else :
            if self.search(nums[middle_index+1:],target) == -1 :
                return -1
            else : 
                return self.search(nums[middle_index+1:],target) + middle_index +1
