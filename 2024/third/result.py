number1 = ''
number2 = ''
mul_str = 'mul('
mul_middle = False
is_one_comma = False
all_mul_start = False
counter = 0
suma = 0
with open('input.txt') as file:
    for ff in file:
        for f in ff:
            #print(f, all_mul_start, mul_middle, is_one_comma,number1,number2)
            if all_mul_start==False and f == mul_str[counter]:
                if counter == 3:
                    all_mul_start = True
                    continue
                counter += 1
            elif all_mul_start and f.isdigit():
                if is_one_comma and mul_middle==False:
                    counter = 0
                    all_mul_start = False
                    mul_middle = False
                    is_one_comma = False
                    number1 = ''
                    number2 = ''
                    continue
                
                if is_one_comma:
                    number2 += f
                else:
                    number1 += f
                mul_middle = True

            elif all_mul_start and f == ',':
                if is_one_comma:
                    counter = 0
                    all_mul_start = False
                    mul_middle = False
                    is_one_comma = False
                    number1 = ''
                    number2 = ''
                    continue
                is_one_comma = True
            elif mul_middle and is_one_comma and f == ')':
                if number2 != '':
                    #print('do mnozenia: ', number1, number2)
                    suma += int(number1) * int(number2)
                    counter = 0
                    all_mul_start = False
                    mul_middle = False
                    is_one_comma = False
                    number1 = ''
                    number2 = ''
            else:
                counter = 0
                all_mul_start = False
                mul_middle = False
                is_one_comma = False
                number1 = ''
                number2 = ''
        
print('suma: ',suma)

