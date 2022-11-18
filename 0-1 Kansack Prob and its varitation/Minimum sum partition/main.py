#User function Template for python3
class Solution:
	def minDifference(self, nums, n):
		Sum = sum(nums)

        Range = Sum // 2
        dp = [[0 for _ in range(Sum + 1)] for _ in range(n + 1)] 

        self.SubsetSum(nums,Sum,dp,n)
        #print(dp)
        validInput = []
        minVal = 1000000000
        
        for i in range(Range+1):
            if dp[n][i] == True:

                val = (Sum - 2 * (i))

                minVal = min(val,minVal)

        return minVal

                


    def SubsetSum(self, nums,Sum, dp,N):

        # Base condition 
        for i in range(N + 1):
            for j in range(Sum + 1):
                
                if i == 0:
                    dp[i][j] = False
                    
                if j == 0:
                    dp[i][j] = True
                    
        #Filling up the table
        for i in range(1,N + 1):
            for j in range(1,Sum + 1):
                
                if j >= nums[i-1]:
                    
                    dp[i][j] =  max(dp[i-1][j-nums[i-1]], dp[i-1][j])
                    
                
                elif j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends
