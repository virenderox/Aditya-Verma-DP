#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        
        #base condition already done
        dp = [[0 for _ in range(W + 1)] for _ in range(N+1)]
        
        #Filling up the table
        #self.unboundedKnapSackTable(N,W,val,wt,dp)
        return self.unboundedKnapSackMemo(W,wt,val,N,{})
        
    def unboundedKnapSackTable(self,N,W,val,wt,dp):
        
        for i in range(1,N+1):
            for j in range(1,W+1):
                
                if j >= wt[i-1]:
                    dp[i][j] = max(val[i-1] + dp[i][j - wt[i-1]] , dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
                    
    def unboundedKnapSackMemo(self,W,wt,val,n,dic):
        
        if n == 0 or W == 0:
            return 0
            
        currentKey = (W,n)
        if currentKey in dic:
            return dic[currentKey]
            
        if W >= wt[n-1]:
            
            dic[currentKey] = max(val[n-1] + self.unboundedKnapSackMemo(W-wt[n-1],wt,val,n,dic), self.unboundedKnapSackMemo(W,wt,val,n-1,dic))
            return dic[currentKey]
            
        elif W < wt[n-1]:
            dic[currentKey] = self.unboundedKnapSackMemo(W,wt,val,n-1,dic)
            return dic[currentKey]
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends
