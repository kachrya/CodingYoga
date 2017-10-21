# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
import math


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        bad = 0
        # if first is bad, then thats the ans
        if isBadVersion(left) is True:
            return 1
        # if only 2, and since first is not bad, check if second is bad
        if n == 2:
            if isBadVersion(right) is True:
                return right

        while right - left > 1:
            # init bad each iteration to either of l or r
            if isBadVersion(left) is True:
                bad = left
            elif isBadVersion(right) is True:
                bad = right
            mid = math.floor((left + right) / 2)
            if isBadVersion(mid) is True:
                right = mid
                bad = mid
            else:
                left = mid
        return int(bad)
