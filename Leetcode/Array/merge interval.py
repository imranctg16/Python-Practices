class Solution:
   def merge(self, intervals: list[list[int]]) -> list[list[int]]:
      intervals.sort(key=lambda x: x[0]) # sort them based on the first value 
      
      result = [intervals[0]]

      for i in range(1,len(intervals)):
        last_data = result[-1]
        if intervals[i][0] <= last_data[1]:
            result.pop()
            #modify the second element then delete the first value 
            start  = min(intervals[i][0],last_data[0])
            end = max(intervals[i][1],last_data[1])
            result.append([start,end])
        else:
            result.append(intervals[i])
      return result

solution = Solution()
nums = [[1,3],[2,6],[8,10],[15,18]]
nums = [[1,4],[4,5]]
answer = solution.merge(nums)
print(answer)
