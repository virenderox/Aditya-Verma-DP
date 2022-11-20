#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, s):
		
		n = len(s)
		return self.solve(s,s,n,n)
		
		
	def solve(self,x,y,n,m):
		
	    dp = [[0 for i in range(m+1)] for j in range(n+1)]
		
	    for i in range(1,n+1):
		    for j in range(1, m + 1):
		        
		        if x[i-1] == y[j-1] and i != j:
		            dp[i][j] = 1 + dp[i-1][j-1]
		            
		        else:
		            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
		            
	    return dp[n][m]
		            
		 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends
