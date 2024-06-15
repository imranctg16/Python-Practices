class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        l,r = 0,0
        while(r<len(nums)):
            if(nums[r]%2==0):
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
            r+=1
        return nums

nums = [3,1,2,4]
solution = Solution()
reslt = solution.sortArrayByParity(nums)
print(reslt)
        