class Solution:

    def lengthOfLongestSubstring(self,string):
        hash_map = {}
        max_length = 0
        current_length = 0
        start = 0 
        end = 0
        for index,character in enumerate(string):
            end = index 
            if character in hash_map and hash_map[character] >=start:
                start = hash_map[character] + 1 
            hash_map[character] = end
            current_length = end - start + 1
            max_length = max(max_length,current_length)
        return max_length
    
string = 'abcabcbb'
# string = 'bbbbb'
# string = "abba"

solution = Solution()
answer = solution.lengthOfLongestSubstring(string)
print(answer)