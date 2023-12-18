dat = open('input15.txt').read().splitlines()

def HASH(string):
    val = 0
    for char in string:
        val += ord(char)
        val = val*17
        val = val % 256
    return val

# PART 1
answer1 = 0
for string in dat[0].split(','):
    answer1 += HASH(string)
    
# PART 2
boxes = {}
for string in dat[0].split(','):
    if '=' in string:
        lens = string[:-2]
        box = HASH(lens)
        focal = string[-1]
        if box not in boxes.keys():
            boxes[box] = [lens+focal]
            continue
        replace=False
        for i, l in enumerate(boxes[box]):
            if l[:-1]==lens:
                boxes[box][i] = lens+focal
                replace=True
        if not replace:
            boxes[box].append(lens+focal)
    elif '-' in string:
        lens = string[:-1]
        box = HASH(lens)
        if box not in boxes.keys():
            continue
        for i, l in enumerate(boxes[box]):
            if l[:-1]==lens:
                boxes[box].pop(i)

answer2 = 0
for box in boxes.keys():
    boxnum = int(box)+1
    for pos, l in enumerate(boxes[box]):
        slotnum = pos+1
        focal = int(l[-1])
        answer2 += (boxnum*slotnum*focal)
            
            
                
        