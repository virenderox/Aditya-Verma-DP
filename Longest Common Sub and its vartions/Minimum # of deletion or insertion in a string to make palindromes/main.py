#User function Template for python3
class Solution:
    def minDeletions(self, Str, n): 
        
        Lps = self.longestPalindromeSubseq(Str)
        minOperation = n - Lps
        return minOperation
        
        
    def longestPalindromeSubseq(self, s):

        reverse_s = s[::-1]
        len_s = len(s)
        len_reverse = len(reverse_s)
        lps = self.Lcs(s,reverse_s,len_s,len_reverse)
        
        return lps


    def Lcs(self,x,y,n,m):

        dp = [[0 for i in range(m+1)] for j in range(n+1)]


        for i in range(1,n+1):
            for j in range(1,m+1):

                if x[i-1] == y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
       
        N = int(input())
        Str = input().strip()
        ob = Solution()
        ans = ob.minDeletions(Str, N)
        print(ans)
# } Driver Code Ends
