dat = open('input2.txt').read().splitlines()
max_dict = {'red': 12, 'green': 13, 'blue': 14}
l = []
for game in dat:
    gamenum = int(game.split(': ')[0].split(' ')[1])
    add = True
    for draw in game.split(': ')[1].split('; '):
        for color in draw.split(', '):
            if int(color.split(' ')[0]) > max_dict[color.split(' ')[1]]:
                add = False
                break
    if add:
        l.append(gamenum)
answer1 = sum(l)

power = []
for game in dat:
    gamenum = int(game.split(': ')[0].split(' ')[1])
    min_dict = {'red': 0, 'green': 0, 'blue': 0}
    for draw in game.split(': ')[1].split('; '):
        for color in draw.split(', '):
            if int(color.split(' ')[0]) > min_dict[color.split(' ')[1]]:
                min_dict[color.split(' ')[1]] = int(color.split(' ')[0])
    power.append(min_dict['red']*min_dict['green']*min_dict['blue'])
answer2 = sum(power)