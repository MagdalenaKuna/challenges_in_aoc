
from copy import deepcopy

def find_loop(tab, guard_column, guard_row):
    sum_loops= 0
    is_guarding = True
    look_up = True
    look_down = False
    look_right = False
    look_left = False
    building_x = 0
    building_y = 0
    s1 = set()

    while is_guarding:
        if look_up and is_guarding:
            look_up = False
            look_right = True
            #s1.add((guard_column,guard_row,'UP'))
            for i in range(guard_column,-1,-1):
                if tab[i][guard_row] == '#':
                    building_x = i+1
                    s1.add((i,guard_row,'UP'))
                    break
                if i == 0:
                    is_guarding = False
                    s1.add((i,guard_row,'UP'))
                    break
                if (i,guard_row,'UP') in s1:
                    return 1
                    is_guarding = False
                    break
                s1.add((i,guard_row,'UP'))
                tab[i][guard_row] += 'UP'
            guard_column = building_x
            #print('guard:', guard_column, guard_row)

        if look_down and is_guarding:
            look_down = False
            look_left = True
            #s1.add((guard_column,guard_row,'DOWN'))
            for i in range(guard_column,len_column):
                if tab[i][guard_row] == '#':
                    building_x = i-1
                    s1.add((i,guard_row,'DOWN'))
                    break
                if i == len_column-1:
                    is_guarding = False
                    s1.add((i,guard_row,'DOWN'))
                    break
                if (i,guard_row,'DOWN') in s1:
                    return 1
                    is_guarding = False
                    break
                s1.add((i,guard_row,'DOWN'))
                tab[i][guard_row] += 'DOWN'
            guard_column = building_x


        if look_right and is_guarding:
            look_right = False
            look_down = True
            #s1.add((guard_column,guard_row,'R'))
            for i in range(guard_row,len_row):
                if tab[guard_column][i] == '#':
                    building_y = i-1
                    s1.add((guard_column,i,'R'))
                    break
                if i == len_row-1:
                    is_guarding = False
                    s1.add((guard_column,i,'R'))
                    break
                if (guard_column,i,'R') in s1:
                    return 1
                    is_guarding = False
                    break
                s1.add((guard_column,i,'R'))
                tab[guard_column][i] += 'R'
            guard_row = building_y

        if look_left and is_guarding:
            look_left = False
            look_up = True
            #s1.add((guard_column,guard_row,'L'))
            for i in range(guard_row,-1,-1):
                if tab[guard_column][i] == '#':
                    building_y = i+1
                    s1.add((guard_column,i,'L'))
                    break
                if i == 0:
                    is_guarding = False
                    s1.add((guard_column,i,'L'))
                    break
                if (guard_column,i,'L') in s1:
                    return 1
                    is_guarding = False
                    break
                s1.add((guard_column,i,'L'))
                tab[guard_column][i] += 'L'
            guard_row = building_y  
    return 0

with open('/home/mag/Documents/advent_of_code/challenges_in_aoc/2024/six/input.txt') as file:
    f = file.read()
    guard = f.find('^')
    line = [list(x) for x in f.split('\n')]
    len_column = len(line)
    len_row = len(line[[0][0]])

    guard_column, guard_row = next((x,y) for x in range(len_column) for y in range(len_row) if line[x][y] == '^')
    gc, gr = guard_column, guard_row
    is_guarding = True
    look_up = True
    look_down = False
    look_right = False
    look_left = False
    is_vertical = True
    building_x = 0
    building_y = 0

    set_of_xy= set()
    sum_loops = 0
    s1 = set()
    while is_guarding:
        if look_up and is_guarding:
            look_up = False
            look_right = True
            #s1.add((guard_column,guard_row,'UP'))
            for i in range(guard_column,-1,-1):
                if line[i][guard_row] == '#':
                    building_x = i+1
                    s1.add((i,guard_row,'UP'))
                    break
                if i == 0:
                    is_guarding = False
                    s1.add((i,guard_row,'UP'))
                    break
                if not (i-1 < 0 or line[i-1][guard_row] == '#'):
                    tab = deepcopy(line)
                    tab[i-1][guard_row] = '#'
                    sum_loops += find_loop(tab, gc, gr)
                s1.add((i,guard_row,'UP'))
                line[i][guard_row] += 'UP'
            guard_column = building_x
            #print('guard:', guard_column, guard_row)

        if look_down and is_guarding:
            look_down = False
            look_left = True
            #s1.add((guard_column,guard_row,'DOWN'))
            for i in range(guard_column,len_column):
                if line[i][guard_row] == '#':
                    building_x = i-1
                    s1.add((i,guard_row,'DOWN'))
                    break
                if i == len_column-1:
                    is_guarding = False
                    s1.add((i,guard_row,'DOWN'))
                    break
                if not (i+1 == len_column or line[i+1][guard_row]=='#'):
                    tab = deepcopy(line)
                    #print(i,guard_row)
                    tab[i+1][guard_row] = '#'
                    sum_loops += find_loop(tab, gc, gr)
                s1.add((i,guard_row,'DOWN'))
                line[i][guard_row] += 'DOWN'
            guard_column = building_x


        if look_right and is_guarding:
            look_right = False
            look_down = True
            #s1.add((guard_column,guard_row,'R'))
            for i in range(guard_row,len_row):
                if line[guard_column][i] == '#':
                    building_y = i-1
                    s1.add((guard_column,i,'R'))
                    break
                if i == len_row-1:
                    is_guarding = False
                    s1.add((guard_column,i,'R'))
                    break
                if not (i+1 == len_row or line[guard_column][i+1]=='#'):
                    tab = deepcopy(line)    
                    tab[guard_column][i+1] = '#'
                    sum_loops += find_loop(tab, gc, gr)
                    #break
                s1.add((guard_column,i,'R'))
                line[guard_column][i] += 'R'
            guard_row = building_y

        if look_left and is_guarding:
            look_left = False
            look_up = True
            #s1.add((guard_column,guard_row,'L'))
            for i in range(guard_row,-1,-1):
                if line[guard_column][i] == '#':
                    building_y = i+1
                    s1.add((guard_column,i,'L'))
                    break
                if i == 0:
                    is_guarding = False
                    s1.add((guard_column,i,'L'))
                    break
                if not (i-1 < 0 or line[guard_column][i-1]=='#'):
                    tab = deepcopy(line)
                    tab[guard_column][i-1] = '#'
                    sum_loops += find_loop(tab, gc, gr)
                s1.add((guard_column,i,'L'))
                line[guard_column][i] += 'L'
            guard_row = building_y
        
        #print(s1)
        #set_of_xy.update(s1)
    
    #print(len(set_of_xy))
    print(sum_loops)
    
    #for i in line:
    #    print(i)

