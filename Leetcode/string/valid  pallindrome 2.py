class Solution:

    def isPallindrome(self,str):
        reverse = str[::-1]
        return reverse == str
    
    def validPalindrome(self, s: str) -> bool: 
        l , r = 0 , (len(s) -1) 
        while l < r:
            print(l,r)
            if s[l] != s[r]:
                return self.isPallindrome(s[l+1:r+1]) or self.isPallindrome(s[l:r])   
            l += 1
            r -= 1
        return True

string = "aaaaaaaxa"
solution = Solution()
result = solution.validPalindrome(string)
print(result)