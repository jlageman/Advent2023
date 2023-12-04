dat = open('input3.txt').read().splitlines()
digits = '0123456789'

def check_number(dat, x, y):
    digits = '0123456789'
    num = dat[y][x]
    locs = [(x,y)]
    if x+1 < len(dat[y]):
        if dat[y][x+1] in digits:
            num = num + dat[y][x+1]
            locs.append((x+1,y))
            if x+2 < len(dat[y]):
                if dat[y][x+2] in digits:
                    num = num + dat[y][x+2]
                    locs.append((x+2,y))
    if x-1 >= 0:
        if dat[y][x-1] in digits:
            num = dat[y][x-1] + num
            if x-2 >= 0:
                if dat[y][x-2] in digits:
                    num = dat[y][x-2] + num
    return int(num), locs

def symbol_neighbor(dat, locs):
    not_symbol = '1234567890.'
    neighbor = False
    for loc in locs:
        x,y = loc
        if y-1 >= 0:
            if dat[y-1][x] not in not_symbol:
                neighbor = True
                break
            if x-1 >= 0:
                if dat[y-1][x-1] not in not_symbol:
                    neighbor = True
                    break
            if x+1 < len(dat[y]):
                if dat[y-1][x+1] not in not_symbol:
                    neighbor = True
                    break
        if neighbor:
            break
        if y+1 < len(dat):
            if dat[y+1][x] not in not_symbol:
                neighbor = True
                break
            if x-1 >= 0:
                if dat[y+1][x-1] not in not_symbol:
                    neighbor = True
                    break
            if x+1 < len(dat[y]):
                if dat[y+1][x+1] not in not_symbol:
                    neighbor = True
                    break
        if neighbor:
            break
        if x-1 >= 0:
            if dat[y][x-1] not in not_symbol:
                neighbor = True
                break
        if x+1 < len(dat[y]):
            if dat[y][x+1] not in not_symbol:
                neighbor = True
                break
        if neighbor:
            break
    return neighbor

l = []
to_search = []
searched = []
for y in range(len(dat)):
    for x in range(len(dat[y])):
        to_search.append((x,y))
for loc in to_search:
    if loc in searched:
        continue
    x,y = loc
    if dat[y][x] == '.':
        continue
    elif dat[y][x] in digits:
        num, locs = check_number(dat, x, y)
        searched.extend(locs)
        if symbol_neighbor(dat, locs):
            l.append(num)        
answer1 = sum(l)                 

def digit_neighbor(dat, loc):
    digits = '1234567890'
    x,y = loc
    nlocs = []
    if y-1 >= 0:
        if dat[y-1][x] in digits:
            nlocs.append((x,y-1))
        if x-1 >= 0:
            if dat[y-1][x-1] in digits:
                nlocs.append((x-1,y-1))
        if x+1 < len(dat[y]):
            if dat[y-1][x+1] in digits:
                nlocs.append((x+1,y-1))
    if y+1 < len(dat):
        if dat[y+1][x] in digits:
            nlocs.append((x,y+1))
        if x-1 >= 0:
            if dat[y+1][x-1] in digits:
                nlocs.append((x-1,y+1))
        if x+1 < len(dat[y]):
            if dat[y+1][x+1] in digits:
                nlocs.append((x+1,y+1))
    if x-1 >= 0:
        if dat[y][x-1] in digits:
            nlocs.append((x-1,y))
    if x+1 < len(dat[y]):
        if dat[y][x+1] in digits:
            nlocs.append((x+1,y))
    return nlocs     

l = []            
to_search = []
for y in range(len(dat)):
    for x in range(len(dat[y])):
        to_search.append((x,y))
for loc in to_search:
    x,y = loc
    if dat[y][x] != '*':
        continue
    else:
        nlocs = digit_neighbor(dat, loc)
        numbers = []
        for nl in nlocs:
            x,y = nl
            num, _ = check_number(dat, x, y)
            numbers.append(num)
        unique_numbers = []
        for num in numbers:
            if num not in unique_numbers:
                unique_numbers.append(num)
        if len(unique_numbers) == 2:    
            l.append(unique_numbers[0]*unique_numbers[1])
answer2 = sum(l)