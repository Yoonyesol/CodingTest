import sys
input = sys.stdin.readline

n, k = map(int, input().split())
h_people = list(input().rstrip())

ans = 0 #먹은 햄버거 개수
for i in range(n):  #모든 리스트를 순회
    if h_people[i] == 'P':  #사람이 있으면
        for j in range(max(0, i-k), min(i+k+1, n)): #왼쪽부터 햄버거가 있는지 찾는다
            if h_people[j] == 'H':  #햄버거가 있다면
                h_people[j] = 'E'   #먹는다
                ans += 1    #먹은 만큼 ans값 증가
                break   #다른 햄버거를 먹지 않게 반복문 종료, 다른 P에게 H를 줄 수 있을지 찾는다.
print(ans)


-------------------
<2차>

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bench = list(input().rstrip())

ans = 0
for i in range(n):
    if bench[i] == 'P':
        # 어차피 왼쪽 구간에서 h 발견하면 break되니까 끊지 말고 +-k구간 전부 반복해서 탐색
        for j in range(max(0, i-k), min(i + k + 1, n)):
            if bench[j] == 'H':
                bench[j] = 0    #먹은 햄버거는 먹음 처리
                ans += 1
                break
print(ans)