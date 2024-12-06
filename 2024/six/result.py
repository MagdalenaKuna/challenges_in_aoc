
with open('input.txt') as file:
    f = file.read()
    guard = f.find('^')
    line = [list(x) for x in f.split('\n')]
    len_column = len(line)
    len_row = len(line[[0][0]])

    guard_column, guard_row = next((x,y) for x in range(len_column) for y in range(len_row) if line[x][y] == '^')
    is_guarding = True
    look_up = True
    look_down = False
    look_right = False
    look_left = False
    is_vertical = True
    building_x = 0
    building_y = 0

    set_of_xy= set()

    while is_guarding:
        s1 = set()
        if look_up:
            look_up = False
            look_right = True
            s1.add((guard_column,guard_row))
            for i in range(guard_column,-1,-1):
                if line[i][guard_row] == '#':
                    building_x = i+1
                    break
                if i == 0:
                    is_guarding = False
                    #break
                s1.add((i,guard_row))
                line[i][guard_row] = 'X'
            guard_column = building_x
            #print('guard:', guard_column, guard_row)

        if look_down:
            look_down = False
            look_left = True
            s1.add((guard_column,guard_row))
            for i in range(guard_column,len_column):
                if line[i][guard_row] == '#':
                    building_x = i-1
                    break
                if i == len_column:
                    is_guarding = False
                    #break
                s1.add((i,guard_row))
                line[i][guard_row] = 'X'
            guard_column = building_x


        if look_right:
            look_right = False
            look_down = True
            s1.add((guard_column,guard_row))
            for i in range(guard_row,len_row):
                if line[guard_column][i] == '#':
                    building_y = i-1
                    break
                if i == len_row:
                    is_guarding = False
                    #break
                s1.add((guard_column,i))
                line[guard_column][i] = 'X'
            guard_row = building_y

        if look_left:
            look_left = False
            look_up = True
            s1.add((guard_column,guard_row))
            for i in range(guard_row,-1,-1):
                if line[guard_column][i] == '#':
                    building_y = i+1
                    break
                if i == 0:
                    is_guarding = False
                    #break
                s1.add((guard_column,i))
                line[guard_column][i] = 'X'
            guard_row = building_y
        
        #print(s1)
        set_of_xy.update(s1)
    
    print(len(set_of_xy))
    #for i in line:
    #    print(i)
