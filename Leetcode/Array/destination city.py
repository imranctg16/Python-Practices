class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        dict = {}
        for path in paths:
            dict[path[0]] = path[1]
        for path in paths:
            if path[1] not in dict:
                return path[1]
        return ''

solution = Solution().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
print(solution)