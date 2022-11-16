class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        N = len(A)
        Sum = B
        
        
        dp = [[0 for _ in range(Sum + 1)] for _ in range(N + 1)]
        
        
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
                
                if j >= A[i-1]:
                    
                    dp[i][j] =  max(dp[i-1][j-A[i-1]], dp[i-1][j])
                    
                
                elif j < A[i-1]:
                    dp[i][j] = dp[i-1][j]
        if dp[N][Sum]:
            return 1
        else:
            return 0
                    
  
                    
        
