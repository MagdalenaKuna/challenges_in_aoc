import itertools

file = open('day1.txt', 'r')
lines = file.readlines()
string_numbers_keys = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
string_numbers_selector = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = []

for line in lines:
    first_number = -1
    first_number_text = ''
    last_number = -1
    last_number_text = ''
    for counter in range(len(line)):
        first_number_text += line[counter]
        last_number_text = line[-(counter+1)] + last_number_text
        if (line[counter].isnumeric() or any(ele in first_number_text for ele in string_numbers_keys)) \
                and first_number == -1:
            if line[counter].isnumeric():
                first_number = int(line[counter])
            else:
                elem = [ele in first_number_text for ele in string_numbers_keys]
                k = list(itertools.compress(string_numbers_selector, elem))
                first_number = k[0]
        if (line[-(counter+1)].isnumeric() or any(ele in last_number_text for ele in string_numbers_keys)) \
                and last_number == -1:
            if line[-(counter+1)].isnumeric():
                last_number = int(line[-(counter+1)])
            else:
                elem = [ele in last_number_text for ele in string_numbers_keys]
                k = list(itertools.compress(string_numbers_selector, elem))
                last_number = k[0]
        if first_number != -1 and last_number != -1:
            numbers.append(first_number*10+last_number)
            break

print(numbers)
print(sum(numbers))
