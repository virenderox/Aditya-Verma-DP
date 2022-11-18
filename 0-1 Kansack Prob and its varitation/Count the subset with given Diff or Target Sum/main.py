class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        Sum = sum(nums)
        n = len(nums)
        if n == 1:
            if nums[0] == abs(target):
                return 1
            else:
                return 0

        totalVal = (Sum + target)
        actualVal =  totalVal// 2

        if totalVal % 2 != 0:
            return 0
        
        s1 =  self.perfectSum(nums,n,actualVal)

        return s1


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
