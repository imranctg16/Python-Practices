class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
      map = {}
      for path in paths:
         map[path[0]] = path[0]
      for path in paths:
         if path[1] not in map:
            return path[1]

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
solution = Solution().destCity(paths)
print(solution)