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

        str_num = str(actual_number)
        s_number = set(list(str_num))
        if len(s_number) == 1 and actual_number>9:
            list_of_invalid_IDs.append(int(actual_number))
            actual_number += 1
            continue

        if result2%2 == 0: 
            half = result2//2
            first_half, second_half = divmod(actual_number,10**half)
            if first_half == second_half:
                list_of_invalid_IDs.append(int(actual_number))
                actual_number += 1
                continue
                
        third,rest_third = divmod(actual_number,10**3)
        pairs,rest_pairs = divmod(actual_number,10**2)
        if third != 0 and (third>=100 and rest_third>=100):
            third_flag = True
        else:
            third_flag = False
        if pairs != 0 and (pairs>=10 and rest_pairs>=10):
            pairs_flag = True
        else:
            pairs_flag = False
        while third_flag or pairs_flag:
            third,rest_third2 = divmod(third,10**3)
            pairs,rest_pairs2 = divmod(pairs,10**2)
            if rest_third != rest_third2:
                third_flag = False
            if rest_pairs != rest_pairs2:
                pairs_flag = False
            if (third == 0 and third_flag) or (pairs == 0 and pairs_flag): 
                list_of_invalid_IDs.append(int(actual_number))
                break
        actual_number += 1
            
print(sum(list_of_invalid_IDs))