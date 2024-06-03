class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i , j = 0, 0
        while (i < len(s)) and (j< len(t)):
            first = s[i]
            second = t[j]
            if(first == second):
                i+=1
            j+=1
        return i == len(s)

s = "ab"
t = "baab"
solution = Solution()
result = solution.isSubsequence(s,t)
print(result)