import sys
n = int(sys.stdin.readline().rstrip())
time = [tuple(map(int ,sys.stdin.readline().split())) for _ in range(n)]
time.sort(key = lambda x : (x[1], x[0]))

answer = 0
endtime = 0 
#endtime = time[0][1]/answer = 1 
# => 틀림 : 반례>처음이 (4,4)인 경우 원래 정답 + 1이 출력된다.
for t in time:
    if(t[0]>=endtime):
        endtime = t[1]
        answer += 1
print(answer)

