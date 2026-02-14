class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ap_nums = set()
        for i in nums :
            if i in ap_nums :
                ap_nums.remove(i)
            else :
                ap_nums.add(i)
        return list(ap_nums)[0]
        