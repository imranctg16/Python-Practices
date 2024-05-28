class Solution:
    def maxSlidingWindow2(self,nums,k):
        left = 0
        right = k - 1
        answer = []
        while right < len(nums):
            max_number = max(nums[left:(right+1)])
            answer.append(max_number)
            left += 1
            right += 1
        return answer
    
    def maxSlidingWindow(self,nums,k):
        eligible = [nums[i] for i in range(k)]
        current_max  = max(eligible)
        answer = [current_max]
        start = k  
        while start < len(nums):
            number = nums[start]
            current_max = max(current_max,number)
            answer.append(current_max)
            start+=1
        return answer
    
nums = [1,3,-1,-3,5,3,6,7]
nums = [1,-1]
k = 3
k = 1
solution = Solution()
result = solution.maxSlidingWindow(nums,k)
print(result)