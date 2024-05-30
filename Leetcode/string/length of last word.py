class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


str = "Hello world!"

solution = Solution()

result = solution.lengthOfLastWord(str)

print(result)