class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        output = []
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
        for i in range(len(nums)):
            modified = i+1
            if modified not in hash_map:
                output.append(modified)
        return output