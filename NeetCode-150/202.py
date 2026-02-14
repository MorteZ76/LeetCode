class Solution:
    def happyProcess (self, n :int) -> int:
        final_num = 0
        final_num += (n % 10) * (n % 10)
        while (n / 10) > 0 :
            n = int(n / 10) 
            final_num += (n % 10) * (n % 10)
        return final_num

        
    def isHappy(self, n: int) -> bool:
        seen_numbers = set() 
        while True :
            if n == 1 :
                return True
            if n in seen_numbers : 
                return False 
            seen_numbers.add(n)
            n = self.happyProcess(n)

            
        