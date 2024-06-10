class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       i, j = 0,0
       answer = ""
       while i<len(word1) and j<len(word2):
           answer += word1[i]
           answer += word2[j]
           i+=1
           j+=1
        
       while i < len(word1):
           answer+= word1[i]
           i+=1
       
       while j < len(word2):
                answer+= word2[j]
                j+=1
       return answer

word1 = "ab"
word2 = "pqrs"
solution = Solution()
res = solution.mergeAlternately(word1,word2)
print(res)