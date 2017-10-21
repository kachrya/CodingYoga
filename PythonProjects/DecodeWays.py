class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        111423
        AAADBC
        KADBC
        AKDBC
        KNBC
        AAADW
        KADW
        AKDW
        KNW

        """
        if s == '' or s is None:
            return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        print (s)
        for i in range(2, len(s)+1):
            first = int(s[i-1: i])
            second = int(s[i-2: i])
            print("i=%r first=%r second=%r" % (i, first, second))
            if 9 >= first >= 1:
                dp[i] += dp[i-1]
            if 26 >= second >= 10:
                dp[i] += dp[i-2]

        print(dp[len(s)], dp)
        return dp[len(s)]

soln = Solution()
soln.numDecodings("1223")