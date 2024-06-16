class Solution:
    def reverseWords(self, s: str) -> str:
        splits = s.split()
        return ' '.join(i[::-1] for i in splits)


s = "Let's take LeetCode contest"
result = Solution().reverseWords(s)
print(result)