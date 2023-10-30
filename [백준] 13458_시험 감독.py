import sys
input=sys.stdin.readline

n = int(input().rstrip())   #교실 수
arr = list(map(int, input().split()))   #학생 수
b, c = map(int, input().split())    #총감독관, 부감독관 감독 학생 수

ans = n  #총 감독관 수=총감독관 수로 초기화(한 반마다 한 명씩)
for i in arr:
    # 한 교실의 학생 중 총감독관이 감독하는 학생 수 제외-> 남은 학생을 부감독관이 감독
    if (i - b) % c == 0:    #감독할 학생이 나누어 떨어지는 경우
        if i - b > 0:   #한 교실의 학생 중 총감독관이 감독하는 학생 수 제외한 값이 0보다 크다면
            ans += ((i - b) // c)   #나눈 몫만큼의 감독관을 배치
    else:   #감독할 학생이 나누어 떨어지지 않는 경우
        if i - b > 0:
            ans += ((i - b) // c) + 1   #부감독관 한 명 추가 배치
print(ans)

#소감
#아이디어는 쉽게 생각해낼 수 있었는데 예외처리(if i - b > 0)하는 데 시간이 걸려서 결국 구글링의 힘을 빌려버렸다...
#총감독관이 한 교실 학생을 모두 감독했고 추가로 감독할 학생이 없다면 ans에 부감독관의 수를 추가할 필요가 없다.
#예외처리는 항상 주의하고, boundary에 있는 값부터 세심하게 살펴보아야겠다.

-----------------
[시간 복잡도 개선]

import sys
input=sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

ans = n
for i in arr:
    i -= b	#미리 i에서 b를 빼주는 방식
    if i > 0:
        if i % c == 0:
            ans += (i // c)
        else:
            ans += (i // c) + 1
print(ans)