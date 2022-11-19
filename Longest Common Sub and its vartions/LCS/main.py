class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        mat = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        return self.Lcs(text1,text2,n ,m ,{})

    def Lcs(self,s1,s2,n,m,mat):

        if n == 0 or m == 0:
            return 0

        currentKey  = (n,m)

        if currentKey in mat:
            return mat[currentKey]


        if s1[n-1] == s2[m-1]:
            mat[currentKey] = 1 + self.Lcs(s1,s2,n-1,m-1,mat)
            return mat[currentKey]

        else:
            mat[currentKey] = max(self.Lcs(s1,s2,n-1,m,mat), self.Lcs(s1,s2,n,m-1,mat))

            return mat[currentKey]
