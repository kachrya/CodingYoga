class Solution(object):


    def add_binary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str

        Given two binary strings, return their sum (also a binary string).

        For example,
        a = "11"
        b = "1"
        Return "100".
        """
        num_char = max(len(a), len(b))
        if len(a) > len(b):
            padded_a = a
            padded_b = '0'* (num_char-len(b))+b
        elif len(b) > len(a):
            padded_b = b
            padded_a = '0' * (num_char-len(a))+a
        else:
            padded_b = b
            padded_a = a
        print(padded_a, padded_b)
        result = ''
        carry = '0'
        for i in range(num_char,0,-1):
            carry, addition = self.addChar(padded_a[i-1], padded_b[i-1], carry)
            result = addition + result
        if carry == '1':
            result = carry + result
        return result

    def addChar(self, char1, char2, carry):
        next_carry = '0'
        if char1 == '0' and char2 == '0':
            addition = '0'
        elif char1 == '1' and char2 == '0':
            addition = '1'
        elif char1 == '0' and char2 == '1':
            addition = '1'
        elif char1 == '1' and char2 == '1':
            addition = '0'
            next_carry = '1'

        if carry == '1':
            if addition == '1':
                addition = '0'
                carry = '1'
            else:
                addition = '1'
                carry = '0'
        if carry == '0':
            if next_carry == '1':
                carry = next_carry

        return carry, addition




soln = Solution()
print(soln.add_binary("0", "0"))
