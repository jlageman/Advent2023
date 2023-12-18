from collections import defaultdict
dat = open('input17.txt').read().splitlines()

maps = {}
for y in range(len(dat)):
    for x in range(len(dat[y])):
        maps[(x,y)] = int(dat[y][x])

# PART 1
dist = {}
dirs = [(1,0), (-1,0), (0,1), (0,-1)]
start = (0,0)
end = (max(maps.keys())[0], max(maps.keys())[1])

dist = defaultdict(lambda: 99999999)
search = [[0, start, (1,0)], [0, start, (0,1)]]

while search:
    d, coords, direction = search.pop(search.index(min(search)))
    if coords == end:
        answer1 = d
        break
    if d > dist[coords, direction]:
        continue
    x, y = coords
    dx, dy = direction
    for ndx, ndy in ((-dy, dx), (dy, -dx)):
        new_d = d
        for steps in range(1,4):
            new_x, new_y = x + ndx*steps, y + ndy*steps
            if 0 <= new_x <= max(maps.keys())[0] and 0 <= new_y <= max(maps.keys())[1]:
                new_d += maps[(new_x, new_y)]
                if new_d < dist[(new_x, new_y), (ndx, ndy)]:
                    dist[(new_x, new_y), (ndx, ndy)] = new_d
                    search.append([new_d, (new_x, new_y), (ndx, ndy)])
                    
# PART 2
dist = {}
dirs = [(1,0), (-1,0), (0,1), (0,-1)]
start = (0,0)
end = (max(maps.keys())[0], max(maps.keys())[1])

dist = defaultdict(lambda: 99999999)
search = [[0, start, (1,0)], [0, start, (0,1)]]

while search:
    d, coords, direction = search.pop(search.index(min(search)))
    if coords == end:
        answer2 = d
        break
    if d > dist[coords, direction]:
        continue
    x, y = coords
    dx, dy = direction
    for ndx, ndy in ((-dy, dx), (dy, -dx)):
        new_d = d
        for steps in range(1,11):
            new_x, new_y = x + ndx*steps, y + ndy*steps
            if 0 <= new_x <= max(maps.keys())[0] and 0 <= new_y <= max(maps.keys())[1]:
                new_d += maps[(new_x, new_y)]
                if steps<4:
                    continue
                if new_d < dist[(new_x, new_y), (ndx, ndy)]:
                    dist[(new_x, new_y), (ndx, ndy)] = new_d
                    search.append([new_d, (new_x, new_y), (ndx, ndy)])



