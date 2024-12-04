
xmas_occurence = 0
is_time_to_end = False
middle_indexes = []

with open('input.txt') as file:
    #f= file.read()
    f = [f for f in file]
    row = len(f[0])-1
    column = len(f)
    counter_row = 0
    counter_column = 0
    for line_f in f:
        for line_ff in line_f:
            
            if f[counter_column][counter_row] == 'X':
                #print(counter_column,counter_row)

                if counter_row - 3 >= 0:
                    if f[counter_column][counter_row-3:counter_row] == 'SAM':
                        xmas_occurence += 1

                if counter_row + 3 < row:
                    if f[counter_column][counter_row + 1:counter_row+4] == 'MAS':
                        xmas_occurence += 1

                if counter_column - 3 >= 0:
                    if f[counter_column-3][counter_row]+f[counter_column-2][counter_row]+f[counter_column-1][counter_row] == 'SAM':
                        xmas_occurence += 1

                if counter_column + 3 < column:
                    if f[counter_column+1][counter_row]+f[counter_column+2][counter_row]+f[counter_column+3][counter_row] == 'MAS':
                        xmas_occurence += 1
# skosy:
                if counter_column - 3 >= 0 and counter_row - 3 >= 0:
                    if f[counter_column-3][counter_row-3]+f[counter_column-2][counter_row-2]+f[counter_column-1][counter_row-1] == 'SAM':
                        xmas_occurence += 1

                if counter_column + 3 < column and counter_row - 3 >= 0:
                    if f[counter_column+1][counter_row-1]+f[counter_column+2][counter_row-2]+f[counter_column+3][counter_row-3] == 'MAS':
                        xmas_occurence += 1

                if counter_column - 3 >= 0 and counter_row + 3 < row:
                    if f[counter_column-3][counter_row+3]+f[counter_column-2][counter_row+2]+f[counter_column-1][counter_row+1] == 'SAM':
                        xmas_occurence += 1

                if counter_column + 3 < column and counter_row + 3 < row:
                    if f[counter_column+1][counter_row+1]+f[counter_column+2][counter_row+2]+f[counter_column+3][counter_row+3] == 'MAS':
                        xmas_occurence += 1
            if f[counter_column][counter_row] == 'A':
                if counter_row - 1 >= 0 and counter_column - 1 >= 0 and counter_row + 1 < row and counter_column + 1 < column:
                    if f[counter_column-1][counter_row-1] == 'S' and f[counter_column+1][counter_row+1] == 'M':
                        middle_indexes.append((counter_column,counter_row))
                    if f[counter_column-1][counter_row-1] == 'M' and f[counter_column+1][counter_row+1] == 'S':
                        middle_indexes.append((counter_column,counter_row))
                    if f[counter_column+1][counter_row-1] == 'S' and f[counter_column-1][counter_row+1] == 'M':
                        middle_indexes.append((counter_column,counter_row))
                    if f[counter_column+1][counter_row-1] == 'M' and f[counter_column-1][counter_row+1] == 'S':
                        middle_indexes.append((counter_column,counter_row))
                
            counter_row += 1
        counter_column += 1
        counter_row = 0

print('xmas_occurence: ',xmas_occurence)
print(len(middle_indexes))
print(len(set(middle_indexes)))
print(len(middle_indexes) - len(set(middle_indexes)))
