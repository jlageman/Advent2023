dat = open('input5.txt').read().splitlines()
dat = [line for line in dat if len(line)>0]
seeds = [int(dat[0].split()[x]) for x in range(1, len(dat[0].split()))]

# PART 1
i = 1
maps = []
for _ in range(7):
    m = []
    if dat[i][0].isalpha():
        i += 1
    while not dat[i][0].isalpha():
        n = [int(x) for x in dat[i].split()]
        m.append([n[1], n[2], n[0]])
        i += 1
        if i >= len(dat):
            break
    m.sort()
    maps.append(m)
    
def transfer(x, m):
    for c in m:
        if not x in range(c[0], c[0]+c[1]):
            continue
        dif = c[0]-c[2]
        x = x - dif
        break
    return x

locations = []
for seed in seeds:
    for i in range(7):
        new_seed = transfer(seed, maps[i])
        seed = new_seed
    locations.append(seed)
answer1 = min(locations)

# PART 2
ranges = []
for i in range(0, len(seeds), 2):
    ranges.append([(seeds[i], seeds[i]+seeds[i+1])])

def transfer_range(r, m, out):
    s, e = r
    output = out
    for c in m:
        if not s in range(c[0], c[0]+c[1]):
            continue
        dif = c[0]-c[2]
        if e in range(c[0], c[0]+c[1]):
            output.append((s-dif, e-dif))
            return output
        else:
            output.append((s-dif, c[0]+c[1]-1-dif))
            s, e = (c[0]+c[1], e)
            output.extend(transfer_range((s,e), m, output))
            return output
    output.append((s,e))
    return output

locations = []
for r in ranges:
    new_ranges = r
    for i in range(7):
        newr = []
        for nr in new_ranges:
            test = transfer_range(nr, maps[i], [])
            newr.extend(test)
        new_ranges = newr
    locations.extend(new_ranges)
    locations.sort()
answer2 = locations[0][0]
