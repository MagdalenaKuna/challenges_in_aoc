first_distance:int = 0
second_distance:int = 0

first_list = []
second_list = []

sum_distances = 0

dict_right_distances = {}

with open('input1.txt') as file:
    for line in file:
        first_number, second_number = line.split()
        first_number = int(first_number)
        second_number = int(second_number)
        first_distance += first_number
        second_distance += second_number
        first_list.append(first_number)
        second_list.append(second_number)
        
        if second_number in dict_right_distances:
            dict_right_distances[second_number] = dict_right_distances[second_number]+1
        else:
            dict_right_distances[second_number] = 1

    first_list.sort()
    second_list.sort()

    for f, s in zip(first_list,second_list):
        sum_distances += abs(s-f)

    print(sum_distances)
print(second_distance-first_distance)
# dlaczego suma nie działa? tyle wyszło: 1689836 - jest różnica, nie można tak zrobić jeżeli lewa wyprzedza prawą.
similarity_sum = 0
for i in first_list:
    similarity_sum += i*dict_right_distances.get(i,0)
print(similarity_sum)
