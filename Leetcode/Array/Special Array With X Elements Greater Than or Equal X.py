class SpecialArray:
    def specialArray(numbers):
        numbers.sort()   
        n = len(numbers)
        
        for x in range(n + 1):
            count = 0
            for num in numbers:
                if num >= x:
                    count += 1
            if count == x:
                return x
    
        return -1

numbers = [3,5]
result = SpecialArray.specialArray(numbers)
print(result)