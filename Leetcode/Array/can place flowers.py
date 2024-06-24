class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length = len(flowerbed)
        i = 0 
        total = n
        while i < length:
           if i > 0 and i+1 < length:
               if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                   flowerbed[i] = 1
                   total -= 1
           elif i == 0 and flowerbed[i] == 0 and i+1 < length and flowerbed[i+1] == 0:
               flowerbed[i] = 1
               total -= 1
           elif i == length-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
               flowerbed[i] = 1
               total -= 1
           i += 1
        return total <= 0
flowerbed = [1,0,0,0,1]
flowerbed = [0]
n = 1
n = 1
result = Solution().canPlaceFlowers(flowerbed,n)
print(result)
        