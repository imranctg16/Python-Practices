class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        answer = []
        flag = False
        first = None
        second = None
        for interval in intervals:

            if newInterval[0] > interval[1]:
                answer.append(interval)
                continue
            if not flag and newInterval[0] < interval[1]:
                first = interval[0]
                flag = True
           
            if flag and newInterval[1] < interval[1]:
                second = interval[1]
                flag = False
                answer.append([first,second])
        return answer
solution = Solution()

# intervals = [[1,3],[6,9]]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]

# newInterval = [2,5]
newInterval = [4,8]
answer = solution.insert(intervals,newInterval)
print(answer)