import string
import random

class Codec:

    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''
            for i in range(6):
                code = code + random.choice(Codec.alphabet)
            #code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        code = shortUrl[-6:]  #slice last 6
        return self.code2url[code]

codec = Codec()
print(codec.encode("https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/"))
print(codec.encode("https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/"))
print(codec.decode(codec.encode("https://leetcode.com/problems/encode-and-decode-tinyurl/")))
