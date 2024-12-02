is_safe: bool = True
safe_report = 0

with open('input.txt') as file:
    for line in file:
        prev_number = None
        increasing: bool = False
        decreasing:bool = False
        is_safe = True
        
        for number in line.split():
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
        
        if is_safe:
            safe_report += 1 
        

print(safe_report)