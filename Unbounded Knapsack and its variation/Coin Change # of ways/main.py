#User function Template for python3

class Solution:
    def count(self, coins, N, Sum):
        
        dp = [[0 for _ in range(Sum+1)] for _ in range(N + 1)]
        
        #base condition 
        for i in range(N+1):
            dp[i][0] = 1
            
        #Filling up the table as based on Unbounded Knapsack Problem
        #Wt -> coin
        #W - > Sum
        
        for i in range(1,N+1):
            for j in range(1,Sum + 1):
                
                if j >= coins[i-1]:
                    
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
                    
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[N][Sum]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends
