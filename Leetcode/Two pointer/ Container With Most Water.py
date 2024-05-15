class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        answer = 0
        left = 0
        right = len(height) -1
        while left < right:
            area = (right - left) * min(height[right],height[left])
            answer = max(area,answer)
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return answer
    
nums = [1,8,6,2,5,4,8,3,7]
nums =  [1,1]
solution = Solution()
answer = solution.maxArea(nums)
print(answer)