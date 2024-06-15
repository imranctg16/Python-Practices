class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


haystack = "hello"
needle = "ll"
solution = Solution()
result = solution.strStr(haystack,needle)
print(result)