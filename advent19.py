dat = open('input19.txt').read().splitlines()
operations = [line for line in dat if len(line)>0 and line[0].isalpha()]
ops = {}
for _ in range(len(operations)):
    op = operations.pop(0)
    name, do = op.split('{')
    ops[name] = do[:-1].split(',')
    
def do_operations(ops, part, op):
    for operation in ops[op]:
        if not ':' in operation:
            return operation
        val = part[operation[0]]
        condition, result = operation.split(':')
        if '>' in condition:
            if val > int(condition.split('>')[1]):
                return result
        elif '<' in condition:
            if val < int(condition.split('<')[1]):
                return result

# PART 1
parts = [line for line in dat if len(line)>0 and line[0]== '{']
parts = [part[1:-1].split(',') for part in parts]
for _ in range(len(parts)):
    part = parts.pop(0)
    p = {}
    for q in part:
        p[q[0]] = int(q[2:])
    parts.append(p)
    
accepted = []
rejected = []
for part in parts:
    o = 'in'
    while not (o == 'R' or o == 'A'):
        o = do_operations(ops, part, o)
    if o == 'R':
        rejected.append(part)
    elif o == 'A':
        accepted.append(part)

answer1 = 0
for part in accepted:
    for q in part.values():
        answer1 += q

# PART 2
def search_outcomes(ops, op, step, ranges):
    
    accepted = 0
    step = step
    operation = ops[op][step]
    
    # if this is final step
    if not ':' in operation:
        if operation == 'A':
            x, m, a, s = ranges.values()
            #print(ranges)
            print('Accepted + ', ((max(x)-min(x))+1)*((max(m)-min(m))+1)*((max(a)-min(a))+1)*((max(s)-min(s))+1))            
            #print('\n')
            return ((max(x)-min(x))+1)*((max(m)-min(m))+1)*((max(a)-min(a))+1)*((max(s)-min(s))+1)
        elif operation == 'R':
            return 0
        else:
            accepted += search_outcomes(ops, operation, 0, ranges)
    
    else:
        # if step is condition
        condition, result = operation.split(':')
        lo, hi = ranges[operation[0]]
    
        if '>' in condition:
    
            # if condition = not true
            r = ranges.copy()
            r[operation[0]] = (lo, min(int(condition.split('>')[1]), hi))
            accepted += search_outcomes(ops, op, step+1, r)
            
            # if condition = true
            r = ranges.copy()
            r[operation[0]] = (max(int(condition.split('>')[1])+1, lo), hi)
            if result == 'A':
                x, m, a, s = r.values()
                #print(r)
                print('Accepted + ', ((max(x)-min(x))+1)*((max(m)-min(m))+1)*((max(a)-min(a))+1)*((max(s)-min(s))+1))
                #print('\n')
                return accepted + ((max(x)-min(x))+1)*((max(m)-min(m))+1)*((max(a)-min(a))+1)*((max(s)-min(s))+1)
            elif result == 'R':
                return accepted + 0
            else:
                accepted += search_outcomes(ops, result, 0, r)
            
        elif '<' in condition:
    
            # if condition = not true
            r = ranges.copy()
            r[operation[0]] = (max(int(condition.split('<')[1]), lo), hi)
            accepted += search_outcomes(ops, op, step+1, r)
            
            # if condition = true
            r = ranges.copy()
            r[operation[0]] = (lo, min(int(condition.split('<')[1])-1, hi))
            if result == 'A':
                x, m, a, s = r.values()
                #print(r)
                print('Accepted + ', ((max(x)-min(x))+1)*((max(m)-min(m))+1)*((max(a)-min(a))+1)*((max(s)-min(s))+1))   
                #print('\n')
                return accepted + ((max(x)-min(x))+1)*((max(m)-min(m))+1)*((max(a)-min(a))+1)*((max(s)-min(s))+1)
            elif result == 'R':
                return accepted + 0
            else:
                accepted += search_outcomes(ops, result, 0, r)

    return accepted        
            
ranges = {'x': (1,4000), 'm': (1,4000), 'a': (1,4000), 's': (1,4000)}
answer2 = search_outcomes(ops, 'in', 0, ranges)


            