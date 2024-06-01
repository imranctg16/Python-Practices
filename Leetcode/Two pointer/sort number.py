# use merge sort algorithm and two pointer technique to merge the arrays 
class Solution:
    def merge_sort(self,nums):
        if(len(nums) == 1):
            return nums
        mid = len(nums) // 2  
        left = nums[:mid]
        right = nums[mid:]
        self.merge_sort(left)
        self.merge_sort(right)

        # merge the arrays 
        i = j = k = 0
        while( i< len(left) and j < len(right)):
            if(left[i] < right[j]):
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        # look for leftover 
        while(i < len(left)):
            nums[k] = left[i]
            i+=1
            k+=1
        
        while(j < len(right)):
            nums[k] = right[j]
            j+=1
            k+=1
        
        return nums


numbers = [5,2,3,1]
numbers = [-2,3,-5]
solution = Solution()
result = solution.merge_sort(numbers)
print(result)

