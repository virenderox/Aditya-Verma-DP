class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        positive_infinity = float('inf')
        n = len(coins)

        #Base condition 
        dp = [[0 for _ in range(amount + 1)] for _ in range(n+1)]
        for i in range(amount + 1):
            dp[0][i] = positive_infinity - 1

        #twist Intiaize first row
        for j in range(1,amount + 1):

            if j % coins[0] == 0:
                dp[1][j] = j // coins[0]
            else:
                dp[1][j] = positive_infinity

        #building table
        for i in range(2,n+1):
            for j in range(1,amount + 1):

                if j >= coins[i-1]:

                    dp[i][j] = min(dp[i][j - coins[i-1]] + 1, dp[i-1][j])

                else:
                    dp[i][j] = dp[i-1][j]
        if dp[n][amount] == positive_infinity:
            return -1

        return dp[n][amount]

        

