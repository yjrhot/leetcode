class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        l1 = len(s) + 1
        l2 = len(t) + 1
        dp = [[1] * l2 for _ in range(l1)]
        
        for j in range(1, l2):
            dp[0][j] = 0
        
        for i in range(1, l1):
            for j in range(1, l2):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
        
