total_numbers = int(input('Total number ?\n'))

number_list = []
answers = []

for i in range(0,total_numbers):
    number_list.append(int(input()))

def create_hash_map(numbers):
    my_map = {}
    for (index,number) in enumerate(numbers):
        my_map[number] = index
    return my_map

hash_map = create_hash_map(number_list)


target_number = int(input('Target Number ?\n'))

print(hash_map)

for (index,number) in enumerate(number_list):
    needed_number = target_number - number;
    if(needed_number in hash_map and hash_map[needed_number]!= index):
        answers.append(index)
        answers.append(hash_map[needed_number])
        break;
print(answers)

