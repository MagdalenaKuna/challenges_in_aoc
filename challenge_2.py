file = open('day2.txt', 'r')
lines = file.readlines()
max_colours = {'red': 12, 'blue': 14, 'green': 13}

games_table = []
single_game = []
game_dict = {}

for line in lines:
    valid_game = True
    game_number, rest = line.split(': ')
    games = rest.split('; ')
    for i in range(len(games)):
        game = games[i].split(', ')
        for j in range(len(game)):
            n, k = game[j].split()
            game_dict[k] = int(n)
            if game_dict[k] > max_colours[k]:
                valid_game = False

    if valid_game:
        game_text, game_num = game_number.split()
        games_table.append(int(game_num))

for i in range(len(games_table)):
    print(type(games_table[i]))

print(sum(games_table))
