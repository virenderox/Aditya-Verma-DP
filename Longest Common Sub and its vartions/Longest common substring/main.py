def PrintLcs(s1,s2,n,m):

    if n == 0 or m == 0:
        return 0

    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):

            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])


    i = n
    j = m

    lsc = ""

    while i > 0 and j > 0:

        if s1[i-1] == s2[j-1]:
            lsc += s1[i-1]
            i -= 1
            j -= 1

        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1

        else:
            j -= 1

    lsc = lsc[::-1]


    return lsc

        
        

