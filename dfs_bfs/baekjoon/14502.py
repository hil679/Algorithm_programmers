from itertools import combinations
from collections import deque
from copy import deepcopy
import sys

def bfs():
    que = deque()
    for x in range(len(labMap)):
        for y in range(len(labMap[0])):
            if labMap[x][y] == 2:
                que.append((x,y))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while que:
        x, y = que.popleft()
        for i in range(len(dx)):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if (0 > next_x or next_x >= n or next_y < 0 or next_y >= m):
                continue
            elif (templabMap[next_x][next_y] == 0):
                templabMap[next_x][next_y] = 2
                que.append((next_x, next_y))
    
    zero = 0
    for i in templabMap:
        zero += i.count(0)
    return zero

n, m = map(int, sys.stdin.readline().rstrip().split())
labMap = list(list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n))
noWall = []
for x in range(len(labMap)):
    for y in range(len(labMap[0])):
        if labMap[x][y] == 0:
            noWall.append((x, y))
wallC = list(combinations(noWall, 3))
answer = 0

for wall in wallC:
    a, b, c = wall
    templabMap = deepcopy(labMap)
    templabMap[a[0]][a[1]],templabMap[b[0]][b[1]],templabMap[c[0]][c[1]] = 1,1,1
    answer = max(answer, bfs())
    templabMap[a[0]][a[1]],templabMap[b[0]][b[1]],templabMap[c[0]][c[1]] = 0,0,0
print(answer)