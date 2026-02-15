class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = 0 
        total_sum = 0
        zero_appeared = False 
        for i in nums: 
            if i > max_num :
                max_num = i
            if i == 0 :
                zero_appeared = True
            total_sum += i
        if zero_appeared == False :
            return 0
        if int((((max_num + 1) * max_num) / 2 ) - total_sum) == 0 :
            return (max_num + 1)
        return int((((max_num + 1) * max_num) / 2 ) - total_sum)
        