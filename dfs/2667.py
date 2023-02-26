n = int(input())#지도 크기
graph = []
vnum = [] #각 단지 집 개수 세기 리스트
for i in range(n):
    graph.append(list(map(int, input())))# NxN자료 받기

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n: #정사각형 벗어난 경우
        return False

    if graph[x][y] == 1:#집 있으면
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            dfs(x_, y_)
        return True
    return False


count = 0#각 단지 수 세기
result = 0#총 단지 수

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            vnum.append(count)
            result += 1
            count = 0

vnum.sort()
print(result)
for i in range(len(vnum)):
    print(vnum[i])