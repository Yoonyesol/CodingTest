import sys
input=sys.stdin.readline

n, x = map(int, input().split())
days = list(map(int, input().split()))

days_sum = sum(days[0:x])   #0~x까지 수의 합계
max_sum = days_sum  #가장 큰 합에 days_sum 대입해 초기화
cnt = 0 #max_sum 개수를 세는 카운트 변수
i = 1   #while문 내에서 인덱스로 사용할 변수
while True:
    if i+x-1 == n:  #n을 벗어난 경우 out of index 발생하므로 미리 처리해줌
        break
    days_sum = days_sum - days[i-1] + days[i+x-1]   #현재 sum에서 가장 처음 인덱스 값을 빼고 다음 인덱스 값을 더해 차례로 순회
    if max_sum < days_sum:  #새로운 max값이 생겼을 때
        max_sum = days_sum  #max값을 초기화
        cnt = 0 #카운트 0으로 초기화
    elif max_sum == days_sum:   #동일한 max값인 경우
        cnt += 1    #max값 카운트
    i += 1  #인덱스+1

if max_sum == 0:    #방문자 없음
    print("SAD")
else:   #방문자 존재
    print(max_sum)  #max값 출력
    print(cnt+1)    #카운트 값 출력(기존에 존재한 하나의 값을 고려하여 1을 추가)
