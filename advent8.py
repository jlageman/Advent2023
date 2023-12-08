dat = open('input8.txt').read().splitlines()
instructions = dat[0]
map_dict = {}
for line in dat[2:]:
    map_dict[line.split(' = ')[0]] = [line.split(' = ')[1][1:4], line.split(' = ')[1][6:9]]

# PART 1
steps = 0
curloc = 'AAA'
while curloc != 'ZZZ':
    for ins in instructions:
        if curloc == 'ZZZ':
            break
        steps += 1
        if ins == 'L':
            curloc = map_dict[curloc][0]
        elif ins == 'R':
            curloc = map_dict[curloc][1]
answer1 = steps
            
# PART 2
from math import lcm
curlocs = [x for x in map_dict.keys() if x[2]=='A']
tarlocs = [x for x in map_dict.keys() if x[2]=='Z']
steps_list = []
for curloc in curlocs:
    steps = 0
    while curloc not in tarlocs:
        for ins in instructions:
            if curloc in tarlocs:
                break
            steps += 1
            if ins == 'L':
                curloc = map_dict[curloc][0]
            elif ins == 'R':
                curloc = map_dict[curloc][1]
    steps_list.append(steps)
answer2 = lcm(*steps_list)
