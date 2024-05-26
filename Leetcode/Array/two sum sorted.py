class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0 
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1,right+1]
            if sum < target:
                left+=1
            if sum > target:
                right -=1

numbers = [2,7,11,15]
target = 9
solution = Solution()
reslt = solution.twoSum(numbers,target)
print(reslt)