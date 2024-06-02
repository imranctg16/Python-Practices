class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums 
    

answer = Solution().getConcatenation([1,2,3])
print(answer)