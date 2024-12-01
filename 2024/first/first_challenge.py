first_distance:int = 0
second_distance:int = 0

first_list = []
second_list = []

sum_distances = 0

with open('input1.txt') as file:
    for line in file:
        first_number, second_number = line.split()
        first_number = int(first_number)
        second_number = int(second_number)
        first_distance += first_number
        second_distance += second_number
        first_list.append(first_number)
        second_list.append(second_number)
    first_list.sort()
    second_list.sort()

    for f, s in zip(first_list,second_list):
        sum_distances += abs(s-f)

    print(sum_distances)
print(second_distance-first_distance)
# dlaczego suma nie działa? tyle wyszło: 1689836 - jest różnica, nie można tak zrobić jeżeli lewa wyprzedza prawą.

