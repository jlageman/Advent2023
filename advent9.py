import numpy as np
dat = open('input9.txt').read().splitlines()
pred1, pred2 = [], []

for line in dat:
  dif = [[int(x) for x in line.split()]]
  while not all(x == 0 for x in dif[-1]):
    dif.append(list(np.diff(dif[-1])))
  dif = list(reversed(dif))
  prev1, prev2 = 0, 0
  for lvl in dif:
    prev1 = lvl[-1] + prev1
    prev2 = lvl[0] - prev2
  pred1.append(prev1)
  pred2.append(prev2)

answer1 = sum(pred1)
answer2 = sum(pred2)
