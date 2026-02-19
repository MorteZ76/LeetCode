class Solution:
    def eligible(self, digits: list, is_negative: bool) -> int:
        i = 2147483648
        if is_negative == False :
            i -= 1
        max_digits = []
        while ( i!= 0) :
            d = i % 10
            i = int (i/10)
            max_digits.append(d)
        if len(digits) < len(max_digits) :
            return True
        if len(digits) > len(max_digits) :
            return False
        for i in range(len(digits)) :
            j=  len(digits)- 1- i
            if digits[i] < max_digits[j] :
                return True
            if digits[i] > max_digits[j] :
                return False
        return True




    def reverse(self, x: int) -> int:
        is_negative = False 
        digits = []
        if x < 0 :
            is_negative = True
        x = abs(x)

        while ( x!= 0) :
            d = x % 10
            x = int (x/10)
            digits.append(d)
        if not self.eligible (digits, is_negative):
            return 0
        out = 0
        i = 0 
        while i < len(digits) :
            out = 10 * out
            out = out + digits[i]
            i += 1
        if is_negative :
            out = out * (-1)
        return out