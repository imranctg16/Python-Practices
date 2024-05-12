class MaxConsecutiveElement:
    def hash_map(self,nums) ->dict:
        hash_map = {}
        for number in nums:
            hash_map[number] = 1
        return hash_map
    def longestConsecutive(self, nums) -> int:
        # O(nlogn) solution, we have optimize without sorting
        nums = sorted(nums)
        max_consecutive = 0
        hash_map = self.hash_map(nums)
        for number in nums:
            temp = number
            current_consecutive = 0
            while(temp in hash_map) :
                current_consecutive += 1
                temp+=1
            max_consecutive  = max(max_consecutive,current_consecutive)
        return max_consecutive
    def longestConsecutive2(self, nums) -> int:
        max_number = 0 
        nums = set(nums)
        for number in nums:
            if(number-1) not in nums:
                #its the start of sequence, now lets see how far it goes
                counter = 0
                temp = number
                while temp in nums:
                    counter+=1
                    temp+=1
                max_number = max(max_number,counter)
        return max_number
    
        
max_consecutive_element = MaxConsecutiveElement()
nums = [100,4,200,1,3,2]

nums =  [0,3,7,2,5,8,4,6,0,1]
print(max_consecutive_element.longestConsecutive2(nums))