class Solution:
    def isPalindrome(self, s: str) -> bool:
        corrected_s = []
        for i in s :
            if i.isalnum() :
                corrected_s.append(i.lower())
        for i in range(len(corrected_s)) :
            if (corrected_s[i] != corrected_s[len(corrected_s) - i -1]) :
                return False 
        return True
        # if not s or len(s) == 1 :
        #     return True
        # found_first_char = False 
        # i = 0
        # while found_first_char == False and i < len(s):
        #     if (s[i].isalnum()) :
        #         found_first_char = True
        #         first_char = i
        #     i += 1
        # found_second_char = False
        # j = len(s)-1
        # while found_second_char == False and j >= 0:
        #     if (s[j].isalnum()) :
        #         found_second_char = True
        #         second_char = j
        #     j -= 1
        
        # if (found_first_char == False) :
        #     return True
        # if (s[first_char].lower() != s[second_char].lower()) :
        #     return False
        # return self.isPalindrome(s[first_char + 1 : second_char])


        