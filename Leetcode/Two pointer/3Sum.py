class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #  To solve the 3Sum problem, you can use a two-pointer approach.
        #  Sort the input array, iterate through each element, and for each element, use two pointers to find the other two elements that sum up to zero.
        #  Make sure to handle duplicates properly.
        nums.sort()
        answer = []
        length = len(nums)
        for index,number in enumerate(nums):
            left = index + 1
            right = length - 1 
            while left < right:
                sum = nums[index] + nums[left] + nums[right]
                if(sum == 0):
                    answer.append([nums[index],nums[left],nums[right]])
                    left += 1
                    right-=1
                elif sum < 0:
                    # we need more bigger number
                    left += 1
                else:
                    # we need more smaller number
                    right -= 1
        return answer
    
    def threeSum2(self,nums: list[int]) -> list[list[int]]:
        #  To solve the 3Sum problem, you can use a two-pointer approach.
        #  Sort the input array, iterate through each element, and for each element, use two pointers to find the other two elements that sum up to zero.
        #  Make sure to handle duplicates properly.
        nums.sort()
        answer = []
        print(nums)
        length = len(nums)
        for index,number in enumerate(nums):
            if(index + 1  < length) and  nums[index] == nums[index+1]:
                continue
            left = index + 1
            right = length - 1 
            while left < right:
                sum = nums[index] + nums[left] + nums[right]
                print(nums[left],nums[right])
                if(sum == 0):
                    answer.append([nums[index],nums[left],nums[right]])
                    left += 1
                    right-=1
                    # we have to move the cursor so that we dont get the same value 
                    while left < right and nums[left] == nums[left+1]:
                            left+=1
                    while left < right and nums[right] == nums[right-1]:
                            right-=1
                elif sum < 0:
                    # we need more bigger number
                    left += 1
                else:
                    # we need more smaller number
                    right -= 1
        return answer

solution = Solution()
nums = [-1,0,1,2,-1,-4]
result = solution.threeSum2(nums)    
print(result)