class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if i<=k:
                time += min(tickets[i],tickets[k])
            else:
                time += min(tickets[i],tickets[k]-1)
                
        return time


tickets = [2,3,2]
k = 2 
result = Solution().timeRequiredToBuy(tickets,k)
print(result)
