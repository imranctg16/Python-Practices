class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
       left_sum = []
       right_sum = []
       for i in range(len(nums)):
           left_sum.append(sum(nums[:i]))
           right_sum.append(sum(nums[i+1:]))
       for i in range(len(nums)):
           if left_sum[i] == right_sum[i]:
               return i
       return -1
         
nums = [1,7,3,6,5,6]
result = Solution().pivotIndex(nums)
print(result)