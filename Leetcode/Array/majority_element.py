total_numbers = int(input('Total number ?\n'))
nums = []

for i in range(0,total_numbers):
    nums.append(int(input()))


def brute_force(nums):
    middle = len(nums)/2 
    counter = {number: nums.count(number) for number in nums}
    answer = None
    for key,value in counter.items():
        if(value > middle):
            answer = key
    print(answer)

def o1(nums):
    middle = len(nums)/2 
    nums.sort()
    counter = 1
    digit =  None
    answer = None
    for number in nums:
        if(digit == number):
            counter+=1
        else:
            counter = 1
        if counter > middle:
            answer = digit 
        digit = number
    return nums[0] if answer is None else answer
print(o1(nums)) 