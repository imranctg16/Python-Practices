class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length = len(flowerbed)
        i = 0 
        total = n
        for i in range(length):
            if(flowerbed[i] == 0):
                pass

        
flowerbed = [1,0,0,0,1]
n = 1
n = 2
result = Solution().canPlaceFlowers(flowerbed,n)
print(result)
        