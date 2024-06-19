class Solution:
    def isMonotonic(self,nums):
       flag = None
       for i in range(len(nums)):
           if i == 0:
               continue
           if flag is None and  nums[i] < nums[i-1]:
               flag = 0 
           elif flag is None and  nums[i] > nums[i-1]:
               flag = 1
               
           if flag == 0 and nums[i] > nums[i-1]:
               return False
           if flag == 1 and nums[i] < nums[i-1]:
               return False
        
       return True

# nums =  [1,3,2]
# nums = [1,2,2,3]
nums = [1,1,0]
result = Solution().isMonotonic(nums)
print(result)