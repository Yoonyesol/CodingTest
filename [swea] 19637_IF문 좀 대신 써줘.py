import sys
input = sys.stdin.readline

n, m = map(int, input().split())
inform1 = []    #호칭 리스트
inform2 = []    #파워 리스트

for i in range(n):
    a, b = input().split()
    b = int(b)
    if inform2 and inform2[-1] == b:    #이전에 저장된 값이 동일하다면 저장하지 않는다.(문제조건)
        continue
    inform1.append(a)
    inform2.append(b)

for i in range(m):
    power = int(input().rstrip())
    left, right = 0, len(inform2)-1 #좌우 좌표 인덱스 초기화
    while left <= right:    #좌 좌표가 우 좌표보다 작은 동안 이분법 진행
        mid = (left + right) // 2   #중앙값
        if power > inform2[mid]:    #파워리스트의 중앙 인덱스 값이 입력받은 수보다 큰 경우
            left = mid + 1  #중앙 상단으로 좌 좌표 이동
        else:   #파워리스트의 중앙 인덱스 값이 입력받은 수보다 작거나 같은 경우
            right = mid - 1 #중앙 하단으로 우 좌표 이동
    print(inform1[right+1])




