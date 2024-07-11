class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_number = ""
        counter = 0 
        prev = ""
        for char in num:
            if prev == char:
                counter +=1 
            else:
                counter = 1
            prev = char 
            if counter == 3:
                max_number = max(max_number,char)
        string = ""
        for i in range(3):
            string += str(max_number)
        return string

num = "6777133339"
# num = "42352338"
result = Solution().largestGoodInteger(num)
print(result)