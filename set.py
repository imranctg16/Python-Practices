number = int(input('How many number ?\n'))

numbers = set()

for i in range(0,number):
    temp = int(input())
    numbers.add(temp)

print(numbers)