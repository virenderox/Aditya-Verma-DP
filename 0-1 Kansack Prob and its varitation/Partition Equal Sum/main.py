class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = sum(nums)
        if Sum % 2 != 0:
            return False
        n = len(nums)
        totalSum = Sum // 2

        

        return self.Subset(nums,totalSum,n)

    
    #we are making function of subset sum
    def Subset(self,nums, Sum, n):

        dp = [[False for _ in range(Sum + 1)] for _ in range(n+1)]
        #print(dp)

        #base condition 
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1,n+1):
            for j in range(1,Sum + 1):

                if j >= nums[i-1]:
                    
                    dp[i][j] =  max(dp[i-1][j-nums[i-1]] ,  dp[i-1][j])
                
                    
                
                elif j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]

        return dp[n][Sum]

