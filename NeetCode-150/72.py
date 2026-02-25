class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2) 
        
        # make the dp
        dp = [[0 for _ in range(n2+1)]  for _ in range(n1+1)] 

        # fix the dp table for 0 length of one word (it means we have to just use delete or insert)
        for i in range(n1+1) :
            dp[i][0] = i
        for i in range(n2+1) :
            dp[0][i] = i
            
        # now fill in the main dp by resolving the last char
        for i in range(1, n1+1) :
                for j in range(1, n2+1) :
                    # if they are the same then we are done :
                    if word1[i-1] == word2[j-1] :
                        dp[i][j] = dp[i-1][j-1]
                    else :
                        #then one need to be deleted or replaced
                        dp [i][j] = min (dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1
        return dp[n1][n2]
                   