
actual_position = 50
max_position = 99
min_position = 0
counter = 0
turns = 0

with open('./R5.txt', 'r') as ways:
    for way in ways:
        wing = way[0]
        distance = int(way[1:])
        if distance > max_position:
            turns = distance // 100
            distance = distance % 100

        if wing == 'R':
            if actual_position + distance > max_position:
                if actual_position + distance == 100:
                    actual_position = 0
                else: 
                    actual_position = actual_position+distance-100
                    turns += 1
            else:
                actual_position = actual_position+distance
        else: 
            if actual_position - distance < 0:
                if actual_position != 0 :
                    turns +=1 
                actual_position = 100 - abs(actual_position - distance)
            else:
                actual_position = actual_position - distance
        
        if actual_position == 0:
            counter += 1
        counter += turns
        turns = 0


print(counter)
