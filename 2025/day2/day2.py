import math

list_of_invalid_IDs = []

IDs = open('./2025/day2/input.txt', 'r')
list_of_ranges_IDs = IDs.read().split(',')
for range in list_of_ranges_IDs:
    first, second = range.split('-')
    second = int(second)
    
    actual_number = int(first)
    while actual_number <= second:
        result = math.log(actual_number,10)
        result2=int(result//1)+1
        if result2%2 != 0:
            actual_number += 1
            continue
        half = result2//2
        first_half, second_half = divmod(actual_number,10**half)
        if first_half == second_half:
            list_of_invalid_IDs.append(int(actual_number))
        actual_number += 1
            
print(sum(list_of_invalid_IDs))