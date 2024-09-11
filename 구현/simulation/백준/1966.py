import sys
from collections import deque
t = int(input())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    importance = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while(importance):
        best = max(importance)
        front = importance.popleft() # 큐의 front를 뽑았으므로
        m -= 1
        if(front == best):
            count += 1
            if m < 0: # m이 0이라는 것은 뽑은 숫자가 내 숫자라는 뜻.
                print(count)
                break
        else:   # 뽑은 숫자가 제일 큰 숫자가 아니면
            importance.append(front) # 제일 뒤로 밀려나게 됨
            if m < 0 :  # 제일 앞에서 뽑히면
                m = len(importance) - 1 # 제일 뒤로 이동
