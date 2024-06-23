class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length = len(flowerbed)
        i = 0 
        total = n
        while(i+1 <= length and total):
            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                total-=1  
            i+=1    
        if total:
            return False
        else:
            return True
        
flowerbed = [0,0,1,0,1]
n = 1
result = Solution().canPlaceFlowers(flowerbed,n)
print(result)
        