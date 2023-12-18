dat = open('input18.txt').read().splitlines()

# PART 1
x,y = 0,0
trench = 0
loop = []
for line in dat:
    instr, steps, _ = line.split()
    if instr == 'R':
        x += int(steps)
    elif instr == 'L':
        x -= int(steps)
    elif instr == 'U':
        y -= int(steps)
    elif instr == 'D':
        y += int(steps)
    loop.append((x,y))
    trench += int(steps)

# count lava
lava = 0
for i in range(len(loop)):
    x1, y1, y2 = loop[i][0], loop[i-1][1] , loop[(i+1)%len(loop)][1]
    lava += x1 * (y1 - y2)
answer1 = abs(lava)//2 + 1 - trench//2 + trench

# PART 2
x,y = 0,0
trench = 0
loop = []
for line in dat:
    _, _, color = line.split()
    if color[-2] == '0':
        x += int(color[2:-2],16)
    elif color[-2] == '1':
        y += int(color[2:-2],16)
    elif color[-2] == '2':
        x -= int(color[2:-2],16)
    elif color[-2] == '3':
        y -= int(color[2:-2],16)
    loop.append((x,y))
    trench += int(color[2:-2],16)
    
# count lava
lava = 0
for i in range(len(loop)):
    x1, y1, y2 = loop[i][0], loop[i-1][1] , loop[(i+1)%len(loop)][1]
    lava += x1 * (y1 - y2)
answer2 = abs(lava)//2 + 1 - trench//2 + trench
    