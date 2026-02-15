class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_nums = set()
        for i in nums :
            if i in seen_nums :
                return True
            seen_nums.add(i)
        return False
        