nums = [1,1,1,2,2,3]
nums = [-1,-1]
nums = [4,1,-1,2,-1,2,3]

k = 2

def characterCount(nums):
    counter = {}
    for number in nums:
        counter[number] = counter.get(number,0) + 1
    return counter
def topKFrequent(nums,k):
    counter = characterCount(nums)
    counter = list(sorted(counter.items(),key=lambda item:item[1],reverse=True))
    keys = [key for key,value in counter[:k]]
    return keys
print(topKFrequent(nums,k))