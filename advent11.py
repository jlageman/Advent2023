dat = open('input11.txt').read().splitlines()

# PART 1
# expand the universe in both directions
rows_added = 0
add_y = {}
for y in range(len(dat)):
    add_y[y] = rows_added
    if not '#' in dat[y]:
        rows_added += 1                
cols_added = 0
add_x = {}
for x in range(len(dat[0])):
    add_x[x] = cols_added
    contains_galaxy = False
    for y in range(len(dat)):
        if dat[y][x]=='#':
            contains_galaxy = True
    if not contains_galaxy:
        cols_added += 1

# locate galaxies        
galaxies = {}
galax_num = 0
for y in range(len(dat)):
    for x in range(len(dat[y])):
        xx = x+add_x[x]
        yy = y+add_y[y]
        if dat[y][x] == '#':
            galax_num += 1
            galaxies[galax_num] = (xx,yy)

# find pairs          
def getPairs(galaxies):
    n = len(galaxies)
    h = set() 
    for i in range(n - 1) :
        for j in range(i + 1, n) : 
            h.add((galaxies[i], galaxies[j]));
    h = list(h)
    h.sort()
    return h
pairs = getPairs(list(galaxies.keys()))    

# compute distances
answer1 = 0
for pair in pairs:
    end, start = galaxies[pair[0]], galaxies[pair[1]]
    dx = abs(end[0]-start[0])
    dy = abs(end[1]-start[1])
    answer1 += dx+dy
    
# PART 2
# relocate galaxies        
galaxies = {}
galax_num = 0
for y in range(len(dat)):
    for x in range(len(dat[y])):
        xx = x+(add_x[x]*999999)
        yy = y+(add_y[y]*999999)
        if dat[y][x] == '#':
            galax_num += 1
            galaxies[galax_num] = (xx,yy)

# compute new distances   
answer2 = 0
for pair in pairs:
    end, start = galaxies[pair[0]], galaxies[pair[1]]
    dx = abs(end[0]-start[0])
    dy = abs(end[1]-start[1])
    answer2 += dx+dy
