
printed_before = {} 
counter = 0
is_checking = False
sum_of_middle_pages = 0
sum_of_middle_pages_sorted = 0

with open('input.txt') as file:
    for line in file:

        if line == '\n':
            is_checking = True
            print(printed_before)
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
                    is_not_correct_sorted = True
                    sorting_counter = 0
                    unsorted_list = line_list[counter:]
                    new_list_part = []
                    print('przed while', unsorted_list)
                    while is_not_correct_sorted:
                        if sorting_counter == len(unsorted_list)-1:
                            is_not_correct_sorted = False

                        num_s = unsorted_list[sorting_counter]
                        l_to_sort = [x for x in printed_before.get(num_s,[]) if x in unsorted_list[sorting_counter:] ]
                        
                        if l_to_sort:
                            max_index = max([unsorted_list.index(x) for x in l_to_sort])
                            value_to_move = unsorted_list.pop(sorting_counter)
                            unsorted_list.insert(max_index,value_to_move)
                            num_s = unsorted_list[sorting_counter]
                            continue
                        sorting_counter += 1

                    new_list_part = line_list[:counter] + unsorted_list
                    #print(line_list)
                    #print(new_list_part)
                    sum_of_middle_pages_sorted += new_list_part[int(l/2)]
                    break
                counter += 1
            
            if is_valid_ordering:
                sum_of_middle_pages += line_list[int(l/2)]
        
#print(printed_before)
print(sum_of_middle_pages)
print(sum_of_middle_pages_sorted)