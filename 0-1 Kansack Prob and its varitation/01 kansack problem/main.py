#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
        dp = [[ 0 for _ in range(W+1)] for _ in range(n + 1 )]
        self.KnapsackBottom(W,wt,val,n,dp)
        return dp[n][W]
        
        
    def KnapsackBottom(self,W,wt,val,n,dp):
        
        #Base condition 
        for i in range(n + 1):
            for j in range(W  + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
        
        #filling up table
        
        for i in range(1,n + 1):
            for j in range(1,W + 1):
                
                if j >= wt[i-1]:
                    #print("in if")
                    dp[i][j] =  max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
                    #print(dp[i][j])
                
                elif j < wt[i-1]:
                    dp[i][j] = dp[i-1][j]
                    #print("in else")
                    #print(dp[i][j])
                    
        #print(dp)
            
        
        #--return self.KnapsackTop(W,wt,val,n,{})
        
    def KnapsackTop(self,W,wt,val,n,dic):
        
        if W == 0 or n == 0:
            return 0
            
        currentKey = (W,n)
        if currentKey in dic:
            return dic[currentKey]
            
        if W >= wt[n-1]:
            
            dic[currentKey] = max(val[n-1] + self.KnapsackTop(W-wt[n-1],wt,val,n-1,dic), self.KnapsackTop(W,wt,val,n-1,dic))
            return dic[currentKey]
            
        elif W < wt[n-1]:
            dic[currentKey] = self.KnapsackTop(W,wt,val,n-1,dic)
            return dic[currentKey]
            
       
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends
