class Solution:
     
     def frequency(self,str):
         counter = {}
         for character in str:
             counter[character] = counter.get(character,0)+1
         return counter
     def is_subset_or_equal(self,dict1, dict2):
        for key, value in dict1.items():
            if key not in dict2 or dict2[key] < value:
                return False
        return True
     def minWindow(self, s: str, t: str) -> str:
        t_counter = self.frequency(t)
        left,right = 0,0
        temp_hash_map = {}
        answer = float('inf')
        answer_string = ''
        while right < len(s):
            character = s[right]
            if character in t_counter:
                temp_hash_map[character] = temp_hash_map.get(character,0)+1
            while self.is_subset_or_equal(t_counter,temp_hash_map):
                current_length = right - left +1 
                if current_length < answer:
                    answer = current_length
                    answer_string = s[left:right+1]
                if s[left] in temp_hash_map:
                    temp_hash_map[s[left]] -=1
                left+=1      
            right+=1
        return answer_string
            


# s = 'bbaac'
# t = 'aba'
s = "ADOBECODEBANC"
t = "ABC"
solution = Solution()
result = solution.minWindow(s,t)
print(result)