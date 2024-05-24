class Solution:
   def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
      intervals.sort(key=lambda x: x[0]) 
      # sort them based on the second value 
      counter = 0
      end = intervals[0]
      for i in range(1,len(intervals)):
        if intervals[i][0] < end[1]:
          counter+=1
          end = [min(intervals[i][0],end[0]),min(intervals[i][1],end[1])]
        else:
           end = intervals[i]
      return counter
   

solution = Solution()
nums = [[1,3],[2,6],[8,10],[15,18]]
nums = [[1,4],[4,5]]
nums = [[1,2],[2,3],[3,4],[1,3]]
nums = [[1,2],[1,3],[2,3],[3,4]]
nums = [[1,2],[1,2],[1,2]]
nums = [[1,2],[2,3],[3,4],[1,3]]
# nums = [[0,2],[1,3],[2,4],[3,5],[4,6]]
# nums = [[1,100],[11,22],[1,11],[2,12]]
nums = [[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]

answer = solution.eraseOverlapIntervals(nums)
print(answer)
