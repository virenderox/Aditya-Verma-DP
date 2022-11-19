class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        #base condition alreday included 
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        self.LcsTable(text1,text2,n,m,dp)
        return dp[n][m]
        #return self.Lcs(text1,text2,n ,m ,{})

    def LcsTable(self,s1,s2,n,m,dp):

        for i in range(1,n+1):
            for j in range(1,m+1):

                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])


