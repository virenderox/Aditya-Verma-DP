class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        len_s = len(s)
        len_t = len(t)

        Len = self.Lcs(s,t,len_s,len_t)

        if Len == len_s:
            return True
        else:
            return False

    def Lcs(self,x,y,n,m):

        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):

                if x[i-1] == y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]
