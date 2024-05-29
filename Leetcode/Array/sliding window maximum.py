from collections import deque


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
    
    def maxSlidingWindow3(self,nums,k):
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
    
    def maxSlidingWindow(self,nums,k):
        # Initialize an empty deque to store indices of elements within the current window
        window = deque()
        result = []
        # Iterate through the input array
        for i, num in enumerate(nums):
            # Remove indices from the front of the deque that are outside the current window
            if window and window[0] == i - k:
                window.popleft()
            
            # Remove indices from the back of the deque whose corresponding elements are smaller than the current element
            while window and nums[window[-1]] < num:
                window.pop()
            
            # Add the index of the current element to the back of the deque
            window.append(i)
            
            # If the window is fully formed, record the maximum element (element at the front of the deque)
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result
    
nums = [1,3,-1,-3,5,3,6,7]
# nums = [1,-1]
k = 3
# k = 1
solution = Solution()
result = solution.maxSlidingWindow(nums,k)
print(result)