class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i,j = 0,0 
        while i < len(g) and j < len(s):
            if(g[i]<s[j]):
                i+=1
            j+=1
        return j

g = [1,2]
s = [1,2,3]
solution = Solution()
result = solution.findContentChildren(g,s)
print(result)