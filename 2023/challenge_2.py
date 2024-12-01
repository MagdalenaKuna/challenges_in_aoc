file = open('day2.txt', 'r')
lines = file.readlines()

games_powers = []
single_game_power = 1

for line in lines:
    game_dict = {}
    single_game_power = 1
    game_number, rest = line.split(': ')
    games = rest.split('; ')
    for i in range(len(games)):
        game = games[i].split(', ')
        for j in range(len(game)):
            n, k = game[j].split()
            if game_dict.get(k, 0):
                if game_dict[k] < int(n):
                    game_dict[k] = int(n)
            else:
                game_dict[k] = int(n)

    for k, v in game_dict.items():
        single_game_power *= v

    games_powers.append(single_game_power)

print(games_powers)
print(sum(games_powers))
