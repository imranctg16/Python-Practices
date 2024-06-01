class Codec:
    def __init__(self) -> None:
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        
        if longUrl not in self.encodeMap:
            code =  self.base + str(len(self.encodeMap) + 1)
            self.encodeMap[longUrl] = code
            self.decodeMap[code] = longUrl

        return self.encodeMap[longUrl]
        
    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]


url = "https://leetcode.com/problems/design-tinyurl"

codec = Codec()
encoded = codec.encode(url)
print(encoded)
decode = codec.decode(encoded)
print(decode)
