class SpecialArray:
    def specialArray(numbers):
        for i in range(len(numbers)):
            counter = 0
            for number in numbers:
                if i >= number:
                    counter += 1
            if counter == i+1:
                return i+1
            
        return -1

numbers = [3,5]
result = SpecialArray.specialArray(numbers)
print(result)