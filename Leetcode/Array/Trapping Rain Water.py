class Solution:
    def trap(self, height: list[int]) -> int:
        leftHightest = [0] * len(height)
        rightHightest = [0] * len(height)
        leftMax = 0
        rightMax = 0
        last = len(height)-1
        answer = 0
        for i in range(len(height)):
            leftMax = max(height[i],leftMax)
            leftHightest[i] = leftMax
            rightMax = max(height[last],rightMax)
            rightHightest[last] = rightMax
            last -= 1
        for i in range(len(height)):
            answer += min(leftHightest[i],rightHightest[i]) - height[i]
        return answer
    
nums = [4,2,0,3,2,5]
nums = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
result = solution.trap(nums)
print(result)

