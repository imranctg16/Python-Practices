class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count+=1
        return count
input = [1,2,3,1,1,3]
result = Solution().numIdenticalPairs(input)
print(result)