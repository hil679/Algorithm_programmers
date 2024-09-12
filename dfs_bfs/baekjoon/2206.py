from collections import deque
import copy

def check_wall(map_arr):
    for x in range(len(map_arr)):
        for y in range(len(map_arr[0])):
            if x == 0 and y == 0:
                continue
            if map_arr[x][y] == 1:
                wall_pos.append((x,y))


n, m = map(int, input().split())
map_arr = [list(map(int, input())) for i in range(n) ] 
wall_pos = deque()
check_wall(map_arr)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

que = deque()
que.append((0,0))
answer = -1

while(wall_pos):
    visited = copy.deepcopy(map_arr)
    visited[0][0] = 1
    wall_x, wall_y = wall_pos.popleft()
    visited[wall_x][wall_y] = 0
    while(que):
        x,y=que.popleft()
        for i in range(len(dx)):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if (next_x < 0 or next_y < 0 or next_x >= n or next_y >=m or visited[next_x][next_y] != 0):
                continue
            if (next_x == n -1 and next_y == m - 1):
                visited[next_x][next_y] = visited[x][y] + 1
                break
            else:
                visited[next_x][next_y] = visited[x][y] + 1
                que.append((next_x, next_y))
        if visited[n - 1][m - 1] != 0:
            que.clear()
            break
    if visited[n - 1][m - 1] != 0: 
        if answer == -1 or answer > visited[n - 1][m - 1]:
            answer = visited[n - 1][m - 1]

print(answer)

