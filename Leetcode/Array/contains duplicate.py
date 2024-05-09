total_numbers = int(input('Total number ?\n'))
nums = []

for i in range(0,total_numbers):
    nums.append(int(input()))


def n_log_n(nums):
    nums.sort()
    previous = None
    for i in range(0,len(nums)):
        number = nums[i]
        print(number, previous)
        if number == previous:
            return True
        previous = number
    return False if previous is None else False 

def o_1(nums):
    # using extra memory 
    hash_set = set()
    for number in nums:
        if number in hash_set:
            return True
        else:
            hash_set.add(number)
    return False

# if(n_log_n(nums)):
#     print('true')
# else:
#     print('false')

if(o_1(nums)):
    print('true')
else:
    print('false')