#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        
        dp = [[-1 for i in range(sum+1)] for j in range(N+1)]
        return self.solve(arr,N-1, sum,dp)
        
    def solve(self,arr,current_i,target,dp):
        
        
        if target == 0:
            return True
            
        if current_i == 0:
            return arr[0] == target
        
        if dp[current_i][target] != -1:
            return dp[current_i][target]
        
        notTaken = self.solve(arr,current_i - 1,target,dp)
        taken = False   
        if arr[current_i] <= target:
            taken = self.solve(arr,current_i - 1,target - arr[current_i],dp)
            
        dp[current_i][target] = taken or notTaken    
            
        return dp[current_i][target]
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends
