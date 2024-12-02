is_safe: bool = True
single_bad_level = 0
safe_report = 0


def check_report(raport):
    prev_number = None
    increasing: bool = False
    decreasing:bool = False
    is_safe = True

    for number in raport:
        number = int(number)
        if prev_number == None:
            prev_number = number
            continue
        
        if prev_number < number:
            increasing = True
        elif prev_number > number:
            decreasing = True
        if increasing==decreasing:
            #print('break reason: increasing==decreasing:')
            is_safe = False
            break
        if prev_number == number: 
            #print('break reason: the same values')
            is_safe = False
            break
        if abs(prev_number - number) >= 4:
            #print('break reason: too big break')
            is_safe = False
            break
        prev_number = number
    return is_safe

with open('input.txt') as file:
    for line in file:
        raport = [int(i) for i in line.split()]

        if check_report(raport):
            safe_report += 1
        else:
            for i in range(len(raport)):
                if check_report(raport[:i]+raport[i+1:]):
                    safe_report += 1
                    break

        

print(safe_report)
