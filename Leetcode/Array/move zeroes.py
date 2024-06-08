class Solution:
    def moveZeroes(self, nums: list[int]):
        count = 0
        index = 0
        for i in range(len(nums)):
            if nums[i] !=  0:
                nums[i-count] = nums[i]
                index +=1
            else:
                count+=1
        for i in range(count):
            nums[index+i] = 0
        return nums 
        

nums = [0,1,0,3,12]
solution = Solution()
result = solution.moveZeroes(nums)
print(result)