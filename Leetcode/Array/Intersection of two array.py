class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hash_map = {}
        for num in nums1:
            hash_map[num] = hash_map.get(num,0) + 1
        result = []
        for num in nums2:
            if num in hash_map and hash_map[num] > 0:
                result.append(num)
                hash_map[num] = - 1
        return result

result = Solution().intersection([1,2,2,1],[2,2])
