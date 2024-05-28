class Solution:

    def character_count(self,str):
        hash_map = {}
        for character in str:
            hash_map[character] = hash_map.get(character,0)+1
        return hash_map
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        s1_counter = self.character_count(s1)
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            s2_counter = self.character_count(s2[left:right+1])
            if s1_counter == s2_counter:
                return True
            left += 1
            right += 1
        return False
s1 = "ab"
s2 = "eidbaooo"
s1= "a"
s2 = "ab"
solution = Solution()
result = solution.checkInclusion(s1,s2)
print(result)