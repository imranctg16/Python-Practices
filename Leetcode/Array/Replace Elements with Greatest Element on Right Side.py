class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        i = len(arr) - 1 
        answer = [0]* (len(arr))
        last = -1 
        max_number = -2
        while(i>=0):
            max_number = max(max_number,last)
            answer[i] = max_number
            last = arr[i]
            i-=1
nums = [17,18,5,4,6,1]
result = Solution().replaceElements(nums)
print(result)