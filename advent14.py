dat = open('input14.txt').read().splitlines()

# construct platform
platform = {}
platform['length'] = len(dat)
platform['movable_rocks'] = []
for y in range(platform['length']):
    for x in range(platform['length']):
        platform[(x,y)] = dat[y][x]
        if dat[y][x] == 'O':
            platform['movable_rocks'].append((x,y))

def roll_rocks(platform, direction):
    dx, dy = direction
    roll = True
    while roll:
        roll = False
        for rock in platform['movable_rocks']:
            x,y = rock
            if y+dy >= 0 and y+dy < platform['length'] and x+dx >= 0 and x+dx < platform['length']:
                if platform[(x+dx, y+dy)] == '.':
                    platform[(x+dx, y+dy)] = 'O'
                    platform[(x, y)] = '.'
                    roll = True
        platform['movable_rocks'] = [key for key in platform.keys() if platform[key]=='O']
    return platform

# PART 1
directions = {'north': (0,-1), 'west': (-1,0), 'south': (0,1), 'east': (1,0)}
platform = roll_rocks(platform, directions['north'])
answer1 = 0
for rock in platform['movable_rocks']:
    x,y = rock
    answer1 += (platform['length']-y)

# PART 2
loads = []
for _ in range(200):
    for direction in directions.values():
        platform = roll_rocks(platform, direction)
    load = 0
    for rock in platform['movable_rocks']:
        x,y = rock
        load += (platform['length']-y)
    loads.append(load)

def find_pattern(loads):
    seqlen = 1
    while True:
        seqlen += 1
        if loads[-1-seqlen:-1] == loads[-1-2*seqlen:-1-seqlen]:
            break
    return loads[-1-seqlen:-1]

pattern = find_pattern(loads)
test = int((1000000000-200)/len(pattern))
test2 = (1000000000-200) - (test*len(pattern))
answer2 = pattern[test2]
