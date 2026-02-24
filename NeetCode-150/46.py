class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        if len(nums) ==1 :
            out = [[nums[0]]]
            return out
        for i in range (len(nums)) :
            new_nums = nums[:i] + nums[i+1:]
            adding_list = self.permute(new_nums)
            for j in adding_list :
                out.append([nums[i]] + j)
        return out
        
        