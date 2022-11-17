#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
		
	    dp = [[0 for _ in range(sum + 1)] for _ in range(n+1)]
		
		#base condition
	    for i in range(sum+1):
		    dp[0][i] = 0
		    
		for i in range(n+1):
		    dp[i][0] = 2 ** (self.find_zeros_in_array(arr[:i+1]))
		mod = 1000000007
		#filling up the table
	    for i in range(1,n+1):
		    for j in range(1,sum+1):
		        
		            
		        
		        
		        if j >= arr[i-1]:
		            
		            dp[i][j]=((dp[i-1][j-arr[i-1]])%mod+(dp[i-1][j])%mod)%mod
		            
		        else:
		            dp[i][j] = dp[i-1][j] % mod
		            
		
		            
		return dp[n][sum]
		
	def find_zeros_in_array(self,arr):
	    return len([x for x in arr if x==0])




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends
