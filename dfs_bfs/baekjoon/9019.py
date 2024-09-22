from collections import deque
n = int(input())
que = deque()
maxNum = 9999
def bfs(goal):
    while que:
        curNum, ans = que.popleft()
        # numCnt = len(str(curNum))
        d = curNum * 2 if curNum * 2 <= maxNum else (curNum * 2) % 10000
        if (d == goal):
            que.clear()
            return ans + "D"
        else:
            if not oldNum[d]:
                oldNum[d] = True
                que.append((d, ans+"D"))
        s = curNum -1 if curNum != 0 else maxNum
        if (s == goal):
            que.clear()
            return ans + "S"
        else:
            if not oldNum[s]:
                oldNum[s] = True
                que.append((s, ans+"S"))
        # l = curNum % (10 ** (numCnt - 1)) * 10 + curNum //(10 ** (numCnt - 1))
        l = curNum % 1000 * 10 + curNum // 1000
        if (l == goal):
            que.clear()
            return ans + "L"
        else:
            if not oldNum[l]:
                oldNum[l] = True
                que.append((l, ans+"L"))
        # r = (curNum % 10) * (10 ** (numCnt - 1)) + curNum // 10
        r = (curNum % 10) * 1000 + curNum // 10
        if (r == goal):
            que.clear()
            return ans + "R"
        else:
            if not oldNum[r]:
                oldNum[r] = True
                que.append((r, ans+"R"))
for i in range(n):
    start, goal = map(int, input().split())
    ans = ""
    oldNum = [False for i in range(10001)] #oldNum append하면 시간 초과, 그리고 새로할 때마다 초기화 필수
    que.append((start, ans))
    oldNum[start] = True
    print(bfs(goal))
