class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        first_nineteen = "one two three four five six seven eight nine ten eleven twelve thirteen " \
                         "fourteen fifteen sixteen seventeen eighteen nineteen".split()

        # note that "ten" is not in below list
        high_tens = "twenty thirty forty fifty sixty seventy eighty ninety".split()

        if num == 0:
            return 'zero'

        def words(n):
            print(n)
            if n == 0:
                return ''
            if n < 20:
                return first_nineteen[n-1]
            if n < 100:
                return high_tens[int(n/10)-2] + ' ' + words(n%10)
            if n < 1000:
                return words(int(n/100)) + ' hundred ' + words(n%100)

            # for count, value in enum { x=1, y=2, z=3}
            for count, value in enumerate(('thousand', 'million', 'billion'), 1):
                if n < 1000 ** (count + 1):
                    return words(int(n / (1000**count))) + ' %s ' % value + words(n % 1000**count)
        return ''.join(words(num))

soln = Solution()
print(soln.numberToWords(1000000000))