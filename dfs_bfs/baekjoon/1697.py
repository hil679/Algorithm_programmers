# from collections import deque

# d = deque()
# a, b = map(int,input().split())
# d.append((a + 1, 1))
# d.append((a - 1, 1))
# d.append((a * 2, 1))

# cur_num, cnt = d.popleft()
# if (a == b):
#     print(0)
# else: 
#     while ((cur_num + 1 != b) and (cur_num - 1 != b) and (cur_num * 2 != b)) :
#         d.append((cur_num + 1, cnt +1))
#         if (cur_num - 1 >= 0):
#             d.append((cur_num - 1, cnt +1))
#         d.append((cur_num * 2, cnt +1))
#         cur_num, cnt = d.popleft()

#     print(cnt + 1)

from collections import deque

n, k = map(int, input().split())
max_num = 100000
visited = [0] * (max_num + 1)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for j in (x-1, x+1, x*2):
            if 0 <= j <= max_num and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)
bfs()

