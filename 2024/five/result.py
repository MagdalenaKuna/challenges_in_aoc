
printed_before = {} 
counter = 0
is_checking = False
sum_of_middle_pages = 0

with open('input.txt') as file:
    for line in file:

        if line == '\n':
            is_checking = True
            continue

        if not is_checking:
            first, second = list(int(x) for x in line.split('|'))
            if printed_before.get(second):
                l_temp = printed_before[second] 
                l_temp.append(first)
                printed_before[second]  = l_temp
            else:
                printed_before[second] = [first]
        
        if is_checking:
            is_valid_ordering = True
            line_list = list(int(x) for x in line.split(','))
            l = len(line_list)
            counter = 0
            for count, num in enumerate(line_list):
                # if any number which should be before is after - not correct ordering pages
                #print(line_list[counter:], printed_before.get(num,[]))
                if any(x in line_list[counter:] for x in printed_before.get(num,[])):
                    is_valid_ordering = False
                    #print(line_list)
                    #print('NOT VALID')
                    break
                counter += 1
            
            if is_valid_ordering:
                sum_of_middle_pages += line_list[int(l/2)]
        
#print(printed_before)
print(sum_of_middle_pages)