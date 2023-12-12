dat = open('input12.txt').read().splitlines()

def check_springs(springs, instr, library):
    # check if answer already exists
    if str(springs) in library.keys():
        if str(instr) in library[str(springs)].keys():
            return library[str(springs)][str(instr)], library
    else:
        library[str(springs)] = {}
    # start counting
    num_options = 0
    # if no more broken springs
    if len(instr)<1:
        if '#' in springs:
            library[str(springs)][str(instr)] = 0
            return 0, library
        else:
            library[str(springs)][str(instr)] = 1
            return 1, library
    # if not enough space
    if len(springs) < (sum(instr) + len(instr)-1):
        library[str(springs)][str(instr)] = 0
        return 0, library
    # check springs
    if springs[0] == '.':
        num, library = check_springs(springs[1:], instr, library)
        num_options += num
    elif springs[0] == '?':
        num, library = check_springs(springs[1:], instr, library)
        num_options += num
        sp_copy = springs.copy()
        sp_copy[0] = '#'
        num, library = check_springs(sp_copy, instr, library)
        num_options += num
    elif springs[0] == '#':
        if '.' in springs[:instr[0]]:
            library[str(springs)][str(instr)] = 0
            return 0, library
        elif instr[0] < len(springs) and springs[instr[0]] == '#':
            library[str(springs)][str(instr)] = 0
            return 0, library
        else:
            num, library = check_springs(springs[instr[0]+1:], instr[1:], library)
            num_options += num
    # return final answer
    library[str(springs)][str(instr)] = num_options    
    return num_options, library

# PART 1          
answer1 = 0
library = {}
for line in dat:
    springs = list(line.split()[0])
    instr = [int(x) for x in line.split()[1].split(',')]
    num, library = check_springs(springs, instr, library)
    answer1 += num

# PART 2
answer2 = 0
for line in dat:
    springs = list(line.split()[0])
    new_springs = springs.copy()
    for _ in range(4):
        new_springs.append('?')
        new_springs.extend(springs)
    new_instr = 5*[int(x) for x in line.split()[1].split(',')]
    num, library = check_springs(new_springs, new_instr, library)
    answer2 += num