N = int(input())
sort_arr = []
for i in range(N):
    sort_arr.append(input().split())
    sort_arr[i][1] = int(sort_arr[i][1])
sort_arr.sort(key=lambda x: x[1]) #print(sort_arr.sort()) -> None

for i in range(N):
    print(sort_arr[i][0])