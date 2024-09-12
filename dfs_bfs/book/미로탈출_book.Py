from collections import deque

N, M = map(int, input().split()) 
graph = []
visited = [[0 for i in range(M)] for j in range(N)]
cur_pos = [0,0]
queue = deque()
queue.append((0,0))
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
visited[0][0] = 1
for i in range(N):
    graph.append(list(map(int, input()))) # 숫자 간 띄어쓰기 X -> input().split() X

#if (N - 1, M - 1), arrive
while queue:
    y, x = queue.popleft()
    # y = pos[0]
    # x = pos[1]
    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i] 
        if ( next_x < 0 or next_y < 0 or next_y >= N or next_x >= M or visited[next_y][next_x] != 0):
            continue # break X
        elif (graph[next_y][next_x] == 0):
            visited[next_y][next_x] = -1
        else:
            queue.append((next_y, next_x))
            visited[next_y][next_x] = visited[y][x] + 1

print(visited[N-1][M-1])



