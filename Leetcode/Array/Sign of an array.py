class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product = 1
        for num in nums:
            if num == 0:
                return 0
            product *= num
        return -1 if product < 0 else 1


result = Solution().arraySign([-1,-2,-3,-4,3,2,1])
print(result)