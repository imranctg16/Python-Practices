class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word  in words:
            if word == word[::-1]:
                return word
        return ''
    
words = ["abc","car","ada","racecar","cool"]
solution = Solution()
result = solution.firstPalindrome()
print(result)