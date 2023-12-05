file = open('day1.txt', 'r')
lines = file.readlines()

numbers = []

for line in lines:
    first_number = -1
    last_number = -1
    # print(line)
    for counter in range(len(line)):
        # print(first_number, last_number, numbers)
        if line[counter].isnumeric() and first_number == -1:
            first_number = int(line[counter])
        if line[-(counter+1)].isnumeric() and last_number == -1:
            last_number = int(line[-(counter+1)])
        if first_number != -1 and last_number != -1:
            numbers.append(first_number*10+last_number)
            break

print(numbers)
print(sum(numbers))
