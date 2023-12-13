dat = open('input13.txt').read().splitlines()
patterns = []
curpat = []
for line in dat:
    if len(line)==0:
        patterns.append(curpat)
        curpat = []
    else:
        curpat.append(line)
patterns.append(curpat)

# PART 1
answer1 = 0
for pat in patterns:
    # search for vertical mirror image
    for x in range(len(pat[0])-1):
        xl_range, xr_range = [],[]
        for i in range(min(x+1, len(pat[0])-1-x)):
            xl_range.append(x-i)
            xr_range.append(x+1+i)
        found = True
        for xl, xr in zip(xl_range, xr_range):
            if not all([pat[y][xl]==pat[y][xr] for y in range(len(pat))]):
                found = False
        if found:
            answer1 += (x+1)
            break
    # search for horizontal mirror image
    if not found:
        for y in range(len(pat)-1):
            yu_range, yd_range = [],[]
            for i in range(min(y+1, len(pat)-1-y)):
                yu_range.append(y-i)
                yd_range.append(y+1+i)
            found = True
            for yu, yd in zip(yu_range, yd_range):
                if not all([pat[yu][x]==pat[yd][x] for x in range(len(pat[0]))]):
                    found = False
            if found:
                answer1 += (y+1)*100
                break

# PART 2
answer2 = 0
for pat in patterns:
    # search for vertical mirror image
    for x in range(len(pat[0])-1):
        xl_range, xr_range = [],[]
        for i in range(min(x+1, len(pat[0])-1-x)):
            xl_range.append(x-i)
            xr_range.append(x+1+i)
        found = 0
        for xl, xr in zip(xl_range, xr_range):
            for y in range(len(pat)):
                if not pat[y][xl]==pat[y][xr]:
                    found += 1
        if found == 1:
            answer2 += (x+1)
            break
    # search for horizontal mirror image
    if not found==1:
        for y in range(len(pat)-1):
            yu_range, yd_range = [],[]
            for i in range(min(y+1, len(pat)-1-y)):
                yu_range.append(y-i)
                yd_range.append(y+1+i)
            found = 0
            for yu, yd in zip(yu_range, yd_range):
                for x in range(len(pat[0])):
                    if not pat[yu][x]==pat[yd][x]:
                        found += 1
            if found==1:
                answer2 += (y+1)*100
                break
            