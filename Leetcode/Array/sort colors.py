class Solution:
    def sortColors(self,nums):
        # 0,1,2
        answer = []
        counter = {}
        for number in nums:
            counter[number] = counter.get(number,0) + 1
        index = 0
        for i in range(0,3):
            if i in counter:
                while(counter[i]):
                    nums[index] = i
                    counter[i] -= 1
                    index+=1
        return nums
solution = Solution()
nums = [2,0,2,1,1,0]# max 300 numbers and they are all 0 , 1, 2
result = solution.sortColors(nums)
print(result)