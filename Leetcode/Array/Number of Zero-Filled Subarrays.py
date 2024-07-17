class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
       count = 0
       zero_count = 0
       for i in range(len(nums)):
           if nums[i] == 0:
               zero_count += 1
           else:
               # i got a non-zero number 
               count+= (zero_count * (zero_count +1)) // 2
               zero_count = 0 
       count+= (zero_count * (zero_count +1)) // 2 # if the array ends with zeros 
       return count 
    
nums = [0,1,0,3,12]
result = Solution().zeroFilledSubarray(nums)
print(result)