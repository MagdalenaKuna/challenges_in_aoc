
total_result = 0

def operations(first, second, op):
    #print(first, second,op)
    if op == '+':
        return first + second
    if op == '||':
        return int(str(first) + str(second))
    return first*second

with open('input.txt') as file:
    for line in file:
        part = line.find(':')
        result = line[:part]
        result = int(result)
        rest = line[part+1:]
        equation = []
        equation_final= []
        for number in rest.split():
            number = int(number)
            if not equation:
                equation.append(number)
                continue
            for part in equation:
                r1 = operations(part, number, '+')
                r2 = operations(part, number,'*')
                r3 = operations(part, number,'||')
                #print(r1,r2)
                equation_final.append(r1)
                equation_final.append(r2)
                equation_final.append(r3)
            equation = equation_final[::]
        #print(result, equation_final)
        if result in equation_final:
            print(result)
            total_result += result
    print(total_result)

