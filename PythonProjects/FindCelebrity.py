# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        celebrity = 0
        for i in range(1, n):
            if knows(celebrity, i):
                # if current celeb knows i, then i might be the celeb
                celebrity = i
        # confirm if celeb is for real
        # from 0-celeb index, if celeb knows anyone, then no celeb
        for i in range(celebrity):
            if knows(celebrity, i):
                return -1
        # from 0-n, if anyone doesn't know celeb, then no celeb
        for i in range(n):
            if not knows(i, celebrity):
                return -1

        return celebrity

