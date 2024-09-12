from collections import deque
n, m = map(int, input().split())
map_arr = [list(map(int, input())) for i in range(n)]
visited = [[[0,0] for y in range(len(map_arr[0]))] for x in range(len(map_arr))]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

que = deque()
que.append((0,0,0))
answer = -1
visited[0][0][0] = 1

while(que):
    x,y,break_wall=que.popleft()
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if (next_x < 0 or next_y < 0 or next_x >= n or next_y >= m or visited[next_x][next_y][break_wall]!= 0):
            continue
        elif (map_arr[next_x][next_y] == 0):
            visited[next_x][next_y][break_wall] = visited[x][y][break_wall] + 1
            que.append((next_x, next_y, break_wall))
        elif (map_arr[next_x][next_y] == 1 and break_wall == 0):
            visited[next_x][next_y][1] = visited[x][y][break_wall] + 1
            que.append((next_x, next_y, 1))
        elif (next_x == n -1 and next_y == m - 1):
            visited[next_x][next_y][break_wall] = visited[x][y][break_wall] + 1
            break
if visited[n - 1][m - 1][0] != 0: 
    if visited[n - 1][m - 1][1] != 0:
        answer = min(visited[n - 1][m - 1][0], visited[n - 1][m - 1][1])
    else:
        answer = visited[n - 1][m - 1][0]
elif visited[n - 1][m - 1][1] != 0:
    answer = visited[n - 1][m - 1][1]

print(answer)

