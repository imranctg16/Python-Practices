

total_numbers = int(input('Total number ?\n'))

number_list = []

for i in range(0,total_numbers):
    number_list.append(int(input()))

def create_hash_map(numbers):
    my_map = {}
    for number in numbers:
        my_map[number] = 1
    return my_map

hash_map = create_hash_map(number_list)


target_number = int(input('Target Number ?\n'))

for (number,index) in number_list:
    needed_number = target_number - number;
    if(hash_map.get(needed_number)):
        print(f"Pair found at index {index}: {number} + {needed_number} = {target_number}")
        break;

# print(number_list,target_number);

