class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d= {}
        new_start = 0
        ans = []
        for i in range(len(nums)) :
            if nums[i] in d :
                d[nums[i]] += 1
                new_start += 1
                nums[i] = -1000001
            else :
                d[nums[i]] = 1
        nums.sort()
        i = new_start
        while i < len(nums) :
            d[nums[i]] -= 1
            j = i
            while j < len(nums) :
                d[nums[j]] -= 1
                k = 0 - nums[i] - nums[j]
                if k in d :
                    d[k] -=1 
                    if d[k] >= 0 and d[nums[i]] >= 0 and d[nums[j]] >= 0  and k >= nums[i] and k >= nums[j]:
                        new_ans = [nums[i], nums[j],0 - nums[i] - nums[j]]
                        ans.append(new_ans)
                    d[k] += 1
                d[nums[j]] += 1
                j += 1
            d[nums[i]] +=1
            i += 1
        return ans
                    
