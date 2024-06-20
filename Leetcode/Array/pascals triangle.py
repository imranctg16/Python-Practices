class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        result = [[1],[1,1]]
        for i in range(2,numRows):
            temp = [1]
            for j in range(1,i):
                number = result[i-1][j-1] + result[i-1][j]
                temp.append(number)
            temp.append(1)
            result.append(temp)
        return result
        


rows = 5
result = Solution().generate(rows)
print(result)
        