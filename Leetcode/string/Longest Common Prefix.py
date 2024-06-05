class Solution:

    def findCommon(self,current,latest):
        if(len(current) > len(latest)):
            current,latest = latest,current

        # find common prefix
        for i in range(min(len(current),len(latest))):
            if(current[i] != latest[i]):
                return current[:i]
        return current
    def longestCommonPrefix(self, strs: list[str]) -> str:
        current_prefix = strs[0]
        for i in range(1,len(strs)):
            string = strs[i]
            current_prefix = self.findCommon(current_prefix,string)
        return current_prefix

strs = ["flower","flow","flight"]
strs  = ["ab", "a"]
solution = Solution()
result = solution.longestCommonPrefix(strs)
print(result)