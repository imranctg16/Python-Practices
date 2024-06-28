class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        first = []
        second = []
        for i in nums1:
            if i not in nums2:
                first.append(i)
        for i in nums2:
            if i not in nums1:
                second.append(i)
        return [first,second]
nums1 = [1,2,3]
nums2 = [2,4,6]
result = Solution().findDifference(nums1,nums2)
print(result)