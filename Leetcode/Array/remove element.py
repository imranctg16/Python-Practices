class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
nums = [3,2,2,3]
val = 3
solution = Solution().removeElement(nums, val)
print(solution,nums[:solution])