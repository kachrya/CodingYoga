class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            #return ctr == 0
            if ctr == 0:
                return True
            else:
                return False

        level = {s}
        while True:
            print("level: %r" % level)
            #first check if input string is directly valid
            #valid will be none if it is not
            valid = list(filter(isvalid, level))
            print("valid %r" % valid)
            #if valid is not none, means input string is valid, just return it
            if valid:
                return valid
            temp = set()
            for s in level:
                for i in range(len(s)):
                    #will create sets of parantheses, leaving out parantheses in "i" position
                    #each time
                    temp.update({s[:i] + s[i+1:]})
            level = temp
            #level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}


soln = Solution()
#print(soln.removeInvalidParentheses("()())"))
#)()), (()), ())), ()()
print(soln.removeInvalidParentheses("()(()((((((((((((((((((((((((((((((((((("))
#print(soln.removeInvalidParentheses("((()"))
#)(()(((((((((((((((((((((((((((((((((((, ((()(((((((((((((((((((((((((((((((((((,
#()()(((((((((((((((((((((((((((((((((((, ()(((((((((((((((((((((((((((((((((((((,
