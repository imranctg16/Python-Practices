class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        i = 0
        hash_map = {}
        hash_map2 = {}
        while(i<len(s)):
            char1 = s[i]
            char2 = t[i]
            if char1 not in hash_map:
                hash_map[char1] = char2
                if char2 in hash_map2 and hash_map2[char2]!= char1:
                    return False
            if char2 not in hash_map2:
                hash_map2[char2] = char1
            i+=1
        i = 0
        new_string = ''
        while(i<len(s)):
            char = s[i]
            new_string += hash_map[char]
            i+=1
        return new_string == t
            
s = "badc"
t ="baba"
print(Solution().isIsomorphic(s,t))