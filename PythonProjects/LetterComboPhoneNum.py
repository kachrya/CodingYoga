class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        ret = [""]
        for c in digits:
            tmp = []
            for y in ret:
                print(c, y)
                for x in dict[c]:
                    tmp.append(y + x)
                    print(tmp)
            ret = tmp

        return ret


soln = Solution()
print(soln.letterCombinations("28"))