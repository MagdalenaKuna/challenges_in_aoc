number1 = ''
number2 = ''
mul_str = 'mul('
mul_middle = False
is_one_comma = False
all_mul_start = False
counter = 0
suma = 0
is_enabled = True
word = ''
counter_d = 0
opt1 = False
opt2 = False

def prRed(skk): print("\033[91m{}\033[00m" .format(skk),sep='',end='')
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk),sep='',end='')

with open('input.txt') as file:
    for ff in file:
        for f in ff:
            if is_enabled:
                prGreen(f)
            else:
                prRed(f)
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
                    opt1 = False    
                    opt2 = False
                    word = '' 
                    counter_d = 0    
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
                    opt1 = False    
                    opt2 = False
                    word = '' 
                    counter_d = 0    
                    continue
                is_one_comma = True
            elif mul_middle and is_one_comma and f == ')':
                if number2 != '' and is_enabled:
                    print('do mnozenia: ', number1, number2)
                    suma += int(number1) * int(number2)
                counter = 0
                all_mul_start = False
                mul_middle = False
                is_one_comma = False
                number1 = ''
                number2 = ''
                opt1 = False    
                opt2 = False
                word = '' 
                counter_d = 0    
            elif f in ['d','o','(',')','n','t',"'"]:
                counter = 0
                word += f
                if counter_d == 0 and word[counter_d] == 'd':
                    counter_d += 1
                elif counter_d == 1 and word[counter_d] == 'o' and word == 'do':
                    counter_d += 1
                elif counter_d == 2 and (word[counter_d] == 'n' or word[counter_d] == '(') and (word == 'don' or word == 'do('):
                    if word[counter_d] == '(':
                        opt1 = True
                    else:
                        opt2 = True
                    counter_d += 1
                elif counter_d == 3 and word[counter_d] == ')' and opt1 and word == 'do()':
                    counter_d += 1
                    is_enabled = True
                    opt1 = False    
                    opt2 = False
                    word = '' 
                    counter_d = 0  
                elif counter_d == 3 and word[counter_d] == '\'' and opt2 and word == 'don\'':
                    counter_d += 1
                elif counter_d == 4 and word[counter_d] == 't' and opt2 and word == 'don\'t':
                    counter_d += 1
                elif counter_d == 5 and word[counter_d] == '(' and opt2 and word == 'don\'t(':
                    counter_d += 1
                elif counter_d == 6 and word[counter_d] == ')' and opt2 and word == 'don\'t()':
                    is_enabled = False  
                    opt1 = False    
                    opt2 = False
                    word = '' 
                    counter_d = 0        
                else:
                    opt1 = False    
                    opt2 = False
                    word = '' 
                    counter_d = 0         
            else:
                counter = 0
                all_mul_start = False
                mul_middle = False
                is_one_comma = False
                number1 = ''
                number2 = ''
                opt1 = False    
                opt2 = False 
                word = '' 
                counter_d = 0   
        
print('suma: ',suma)

