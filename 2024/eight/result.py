
dict_of_antinodes = {}
dict_of_anthenas_positions = {}
file = open('input.txt')
f = file.read()
l_col = len(f.splitlines())
for x, line in enumerate(f.splitlines()):
    for y, sign in enumerate(line):
        if sign == '.':
            continue
        if not dict_of_anthenas_positions.get(sign):
            dict_of_anthenas_positions[sign] = [(x, y)]
            continue
        last_one = (x,y)
        for i in dict_of_anthenas_positions.get(sign):
            a,b = i
            print(a,b,x,y)
            antinode_one_x = a - abs(a-x)
            antinode_two_x = x + abs(a-x)
            if b >= y :
                antinode_one_y = b + abs(b-y)
                antinode_two_y = y - abs(b-y)
            else:
                antinode_one_y = b - abs(b-y)
                antinode_two_y = y + abs(b-y)
            if not dict_of_antinodes.get(sign):
                dict_of_antinodes[sign] =  set()
            if not (antinode_one_x < 0 or antinode_one_x >= l_col or antinode_one_y < 0 or antinode_one_y >= len(line)):
                dict_of_antinodes[sign].add((antinode_one_x,antinode_one_y))
            if not (antinode_two_x < 0 or antinode_two_x >= l_col or antinode_two_y < 0 or antinode_two_y >= len(line)):
                dict_of_antinodes[sign].add((antinode_two_x,antinode_two_y))
            #print(sign,dict_of_antinodes)
        dict_of_anthenas_positions[sign].append((x,y))

total_untinodes = set()
sum_of_antinodes = 0


for k, v in dict_of_antinodes.items():
    print(v)
    total_untinodes.update(v)

for x, line in enumerate(f.splitlines()):
    for y, sign in enumerate(line):
        if (x,y) in total_untinodes:
            print('#',end='')
        else:
            print(sign, end='')
    print('')

print(len(total_untinodes))