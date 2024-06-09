class Solution:

    def simulate(self,str):
        stack = []
        for i in range(len(str)):
            if str[i] == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(str[i])
        return stack
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.simulate(s)
        t = self.simulate(t)
        print(s,t)
        return s == t

s = "a##c"
t = "#a#c"
solution = Solution()
result = solution.backspaceCompare(s,t)
print(result)