class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        final_num = "0"
        if num1 == "0" or num2 == "0" :
            return final_num
        def addStrings (num1, num2, num1_offset, num1_mult) :
            num3 = "" 
            remainder = 0
            for i in range (max(len(num1) + num1_offset,len(num2))) :
                number1 = 0
                number2 = 0
                if i < num1_offset :
                    number1 = 0
                if i >= num1_offset and i < len(num1) + num1_offset :
                    number1 = int(num1[len(num1) - 1 -  i + num1_offset]) * num1_mult
                if i < len(num2) :
                    number2 = int(num2[len(num2) - 1 -i]) 
                number1 += remainder
                remainder = (number1 + number2) // 10
                num3 = str((number1 + number2) % 10) + num3
            if remainder > 0 :
                num3 = str(remainder) + num3
            return num3 
        for i in range(len(num2)) :
            final_num = addStrings(num1, final_num, i, int(num2[len(num2) - 1 -i]))
        return final_num



        