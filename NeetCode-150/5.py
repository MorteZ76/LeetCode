class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 :
            return s
        mx_dp = 1
        mx_str_begin = 0
        mx_str_end = 1
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s)) :
            dp[i][i] = 1
        j =1 
        while j < len(s) :
            i = 0 
            while i + j < len(s) :
                dp[i][i+j] = max(dp[i+1][i+j],dp[i][i+j-1])
                if s[i] == s[i+j] :
                    if  dp[i+1][i+j-1] == j -1 :
                        dp[i][i+j] = j + 1
                if dp[i][i+j] > mx_dp :
                    mx_dp = dp[i][i+j] 
                    mx_str_begin = i
                    mx_str_end = i + j + 1
                i += 1
            j +=1
        return s[mx_str_begin:mx_str_end]
        
                

        