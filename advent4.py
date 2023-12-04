dat = open('input4.txt').read().splitlines()
l = []
for line in dat:
    winning = line.split(' | ')[0].split(': ')[1].split(' ')
    winning = [x for x in winning if len(x)>0]
    have = line.split(' | ')[1].split(' ')
    firstnum = True
    points = 0
    for num in have:
        if num in winning:
            if firstnum:
                points = 1
                firstnum = False
            else:
                points = 2*points
    l.append(points)
answer1 = sum(l)

import math
copies = [1] * len(dat)
for y in range(len(dat)):
    for _ in range(copies[y]):
        if l[y] < 2:
            wins = l[y]
        else:
            wins = int(math.log2(l[y])+1)
        for z in range(1,wins+1):
            copies[y+z] += 1
answer2 = sum(copies)