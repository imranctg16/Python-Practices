class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_map = {}
        for char in text:
            hash_map[char] = hash_map.get(char,0) + 1
        balloon = {'b':1,'a':1,'l':2,'o':2,'n':1}
        min_ballon = float('inf')
        for char, count in balloon.items():
            if char not in hash_map:
                return 0
            min_ballon = min(min_ballon,(hash_map[char] // count))
        return min_ballon
    
text = "nlaebolko"
result = Solution().maxNumberOfBalloons(text)
print(result)