class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if(len(words) != len(pattern)):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(words)):
            match = pattern[i]
            word = words[i]
            if match not in dict1:
                dict1[match] = word
            if word not in dict2:
                dict2[word] = match
            if(dict1[match] != word or dict2[word] != match):
                return False
        return True

s = "dog cat cat fish"
pattern = "abba"
result = Solution().wordPattern(pattern,s)
print(result)
