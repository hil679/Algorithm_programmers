#1713번 

import sys
input = sys.stdin.readline

n = int(input())
student = int(input())#총 추천 횟수
num = list(map(int, input().split(" "))) #추천 받은 후보자-key가 됨

photo = dict()
for i in range(student) :
    if num[i] in photo :#후보자가 있으면 
        photo[num[i]][0] += 1 #추천수 +1
    else : #후보자 없으면
        if len(photo) < n : #사진 틀의 개수보다 추천된 후보자 수가 더 적을 때 
            photo[num[i]] = [1, i] # 추천 수 1로 새로 value입력해줌, [추천수, 들어온 순서]
        else : #사진틀의 개수가 부족할 때, 새로 들어온 후보자는 무조건 사진틀에 들어가야 함
            del_list = sorted(photo.items(), key= lambda x : (x[1][0] , x[1][1]) )#추천 수로 sort, 같으면 들어온 순서로 sort => 모두 오름차순
            del_key = del_list[0][0] #가장 앞 = 가장 적은 추천수 + 가장 오래된 사진
            del(photo[del_key]) #삭제
            photo[num[i]] = [1, i] #새 후보자 사진틀에 넣기

ans_list = list(sorted(photo.keys()))#오름차순 정렬
answer = str(ans_list[0])#일렬 출력을 위해 가장 처음 요소 str로
for i in ans_list[1: ] :#일렬 output-0번이 아닌 1번부터 끝까지 더함
    answer += " " + str(i)
print(answer)