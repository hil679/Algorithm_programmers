import sys
from collections import deque

n, m =  map(int,sys.stdin.readline().split())
n_list= list(int(sys.stdin.readline()) for i in range(n)) #단위 무게당 요금
m_list = list(int(input()) for i in range(m)) # 차량들의 무게를 나타내는 정수

allowCar = [0 for i in range(n)]
leftCar = deque() #대기 공간
answer = 0
for j in range(m*2):#들어가고 나오는 수까지 합쳐서
    i = int(sys.stdin.readline())
    if(i>0): #0보다 큰 경우(차가 들어오는 경우)
        if((0 in allowCar)):
            answer += n_list[allowCar.index(0)] * m_list[i - 1] #index는 0부터 시작
            allowCar[allowCar.index(0)] = i
        elif((0 not in allowCar)):
            leftCar.append(i) #자리가 없으면 대기 공간으로 
    else:# 차가 나가는 경우
        allowCar[allowCar.index(abs(i))] = 0 # 차가 나갈 때는 음수니까 절댓값
        if(len(leftCar) != 0):
            popCar = leftCar.popleft()
            answer += n_list[allowCar.index(0)] * m_list[popCar -1] #나가면 queue에 저장되어 있던 거 가져와서 주차요금 계산
            allowCar[allowCar.index(0)] = popCar #다시 만차로 정정
print(answer)