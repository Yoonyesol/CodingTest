import sys
input = sys.stdin.readline

sik = input().rstrip().split("-")   #-기준으로 문자열 분리
total = 0   #식의 결과
for i in range(len(sik)):   #-기준으로 분리된 문자열을 하나씩 확인
    a = list(map(int, sik[i].split("+")))   #문자열 내부에 +가 있다면 + 기준으로 숫자들을 분리
    if i == 0:  #가장 처음 문자는 숫자라는 조건이 있으므로, 가장 처음 문자는 음수가 아니다. 따라서 분리된 수의 총합을 total에 더해준다.
        total += sum(a)
        continue
    total -= sum(a) #0번 인덱스가 아니라면, 분리된 숫자의 총합을 total에서 빼준다.
print(total)

#핵심 아이디어: - 뒤에 나오는 +를 다 괄호로 묶어서 -할 수를 크게 만들자.

#--------------------------
# 25.05.23
sick = input().split('-')
cnt = 0
for i in range(len(sick)):
    b = list(map(int, sick[i].split("+")))
    if i == 0:
        cnt += sum(b)
    else:
        cnt -= sum(b)
print(cnt)
