class Solution:

    def is_overlapping(self,interval,newInterval) -> bool:
        if(newInterval[0] < interval[1] and newInterval[1] >= interval[0]):
            return True
        return False
    
    def merge_interval(self,interval,newInterval) ->list[int]:
        return [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
    
    
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        n = len(intervals)
        i = 0
        res = []

        # Case 1: No overlapping before merging intervals
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Case 2: Overlapping and merging intervals
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Case 3: No overlapping after merging newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

    def insert2(self,intervals,newInterval):
        pass

solution = Solution()

intervals = [[1,3],[6,9]]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# intervals = [[1,5]]

# newInterval = [2,5]
newInterval = [4,8]
# newInterval = [5,7]

answer = solution.insert(intervals,newInterval)
print(answer)