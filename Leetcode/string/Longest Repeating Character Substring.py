class Solution:

     def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = 0
        hash_map = {}
        max_character = 0
        max_length = 0

        while (right < len(s)):
            character = s[right]
            hash_map[character] = hash_map.get(character,0)+1
            max_character = max(hash_map.values())
            sub_string_length = right - left + 1
            if(sub_string_length - max_character > k ):
                hash_map[s[left]] -= 1 # we have to shrink the hash_map as well otherwise we will get max_character wrong  
                left+=1

            max_length = max(max_length,(right-left +1))
            right += 1
        return max_length
     
string = 'AAAA'
k = 2 
solution = Solution()
result = solution.characterReplacement(string,k)
print(result)