#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        
        # step 1 -> intiliaze i and j
        return self.solve(arr,1,N-1, {})
        
    def solve(self,arr,i,j, dic):
        
        ans = float("inf")
        
        #step 2 -> base condition 
        if i == j :
            return 0
            
        #initiliaze the dic
        currentKey = (i,j)
        
        #checking if alredy exit in map
        if currentKey in dic:
            return dic[currentKey]
        
        #step 3 - > K loop
        for k in range(i,j):
            #step 5 -> fun(tmp) -> ans
            ans = min(ans,self.solve(arr,i,k,dic) + self.solve(arr,k+1,j,dic) + (arr[i-1] * arr[k] * arr[j]))
        dic[currentKey] = ans
            
        return dic[currentKey]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends
