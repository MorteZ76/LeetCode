class Solution:
    def search(self, nums: List[int], target: int) -> int:
        o = self.findOffset (nums)
        mn = 0 
        mx = len(nums) - 1
        n = len(nums) 
        while nums[(mn + o) % n ] <= nums[(mx + o) % n]  and mx >= mn:
            mid = (mn + mx) //2 
            if nums[(mid + o) % n]  == target :
                return (mid+ o) % n 
            if nums[(mid + o) % n]  > target :
                mx = mid - 1 
            else : 
                mn = mid + 1
        return - 1



    
    def findOffset(self, nums)  :
        mn = 0
        mx = len(nums) - 1
        if  mn == mx : #it means we have len(nums) == 1
            return 0
        while (mx - mn) > 1: 
            mid = (mx + mn) // 2
            if nums[mid] < nums[mx] :
                mx = mid
            else : 
                mn = mid + 1
        if nums[mn] > nums[mx] :
            return mx
        return mn 

        