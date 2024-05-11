nums = [3,2,4,2]
nums = [1,2,3,4]
nums = [-1,1,0,-3,3]



def productExceptSelf(nums):
    result = []
    length = len(nums)
    for i in range(0,length):
        selfIndex = i
        traverseIndex = 0
        sum = 1
        while(traverseIndex < length):
            if(traverseIndex == selfIndex):
                traverseIndex += 1
                continue
            sum *= nums[traverseIndex]
            traverseIndex += 1
        result.append(sum)
    return result

def productExceptSelf(nums):
    length = len(nums)
    prefix = [1] * length
    suffix = [1] * length 
    result = []
    for i in range(0,len(nums)):
        if i == 0:
            prefix[i] = 1
        else:
            prefix[i] = prefix[i-1] * nums[i-1] 
            
    for i in range(len(nums)-1,-1,-1):
        if i == (len(nums)-1):
            suffix[i] = 1
        else:
            suffix[i] = suffix[i+1]*nums[i+1]
    for i in range(0,len(nums)):
        result.append(prefix[i]*suffix[i])
    return result
print(productExceptSelf(nums))