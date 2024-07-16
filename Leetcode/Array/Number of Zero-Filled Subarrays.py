class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            if num == 0:
                count+=1
        return count
nums = [0,1,0,3,12]
result = Solution().zeroFilledSubarray(nums)
print(result)