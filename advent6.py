dat = open('input6.txt').read().splitlines()
times = [int(x) for x in dat[0].split()[1:]]
distances = [int(x) for x in dat[1].split()[1:]]
win_list = []
for time, distance in zip(times, distances):
    wins = 0
    for i in range(1,time):
        dist = (time - i) * i
        if dist > distance:
            wins += 1
    win_list.append(wins)
import numpy as np
answer1 = np.prod(win_list)

time = int(dat[0].split()[1]+dat[0].split()[2]+dat[0].split()[3]+dat[0].split()[4])
distance = int(dat[1].split()[1]+dat[1].split()[2]+dat[1].split()[3]+dat[1].split()[4])
wins = 0
for i in range(1,time):
    dist = (time - i) * i
    if dist > distance:
        wins += 1
answer2 = wins