total_numbers = int(input('Total number ?\n'))
number_list = []
maxProfit = 0
for i in range(0,total_numbers):
    number_list.append(int(input())) 

left_index = 0
right_index = 1


while(right_index < len(number_list)):

    if(number_list[left_index] < number_list[right_index]):
        profit = number_list[right_index] - number_list[left_index]
        maxProfit = max(maxProfit,profit)
    else:
        left_index = right_index
    
    right_index += 1
print(maxProfit)