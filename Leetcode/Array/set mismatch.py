class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
       nums.sort()
       hash_map = {}
       for i in range(len(nums)):
           hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
       missing = None
       duplicate = None
       counter = 1
       while(counter <= len(nums)):
           if counter not in hash_map:
               missing = counter
           elif hash_map[counter] > 1:
               duplicate = counter
           counter += 1
              
       return [duplicate,missing]
           

nums = [6, 2, 2, 4]
nums = [3,2,3,4,6,5] 
nums = [1,1]
# nums = [1,2,2,4]
result = Solution().findErrorNums(nums)
print(result)