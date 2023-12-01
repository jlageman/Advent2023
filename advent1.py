dat = open('input1.txt').read().splitlines()
digits = '123456789'
l = []
for line in dat:
    d = []
    for item in line:
        if item in digits:
            d.append(item)
    l.append(int(d[0]+d[-1]))
answer1 = sum(l)            

words = {'one': '1', 'two': '2', 'three': '3', 'four': '4',  'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
l = []
for line in dat:
    ind = []
    w_ind = []
    for num in (list(words.keys()) + list(digits)):
        prev_n = 0
        while True:
            part = line[prev_n:]
            n = part.find(num)
            if n != -1:
                ind.append(prev_n + n)
                w_ind.append(num)
                prev_n += n+1
            else:
                break
    first = w_ind[ind.index(min(ind))]
    if len(first)>1:
        first = words[first]
    last = w_ind[ind.index(max(ind))]
    if len(last)>1:
        last = words[last]
    l.append(int(first+last))
answer2 = sum(l)
    