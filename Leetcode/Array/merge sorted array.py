class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(nums1[:])
        nums1[:] = nums1[:m]+nums2
        nums1.sort()
        return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
result = solution.merge(nums1,m,nums2,n)
print(result)