bank_max = []
batteries_max1 = 0
batteries_max2 = 0

with open('./2025/day3/input.txt','r') as bank:
    for batteries in bank:
        batteries_lenght = len(batteries)
        batteries_max1 = batteries[0]
        batteries_max2 = batteries[1]
        for iterator, battery in enumerate(batteries[2:],2):
            if batteries_max2 == 0 and batteries_lenght-1 == iterator:
                batteries_max2 = battery
            if battery > batteries_max1:
                if iterator < batteries_lenght-2:
                    if batteries_max2 < battery:
                        batteries_max1 = battery
                        batteries_max2 = '0'
                    else:
                        batteries_max1 = batteries_max2
                        batteries_max2 = battery                        
                    continue
            if battery > batteries_max2:
                batteries_max2 = battery

        bank_max.append(int(batteries_max1+batteries_max2))

print(sum(bank_max))            

# 17257
# ... 
# 17279