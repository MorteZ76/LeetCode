class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add_one = True
        i = len(digits) - 1
        while i >= 0:
            if add_one == True :
                digits[i] = digits[i] + 1
                add_one = False
            if digits[i] == 10 :
                add_one = True 
                digits[i] = 0
            i -= 1
        if add_one == False :
            return digits 
        else :
            return [1] + digits
            