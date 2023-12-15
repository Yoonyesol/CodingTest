import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))
check = dict()  #0~9번호별 등장횟수 카운트 딕셔너리

for i in range(0, 10):  #0~9번호별 등장횟수 카운트
    check[i] = n.count(i)

maxCheck = max(check, key=check.get)    #가장 큰 value를 가진 key찾아내기
if maxCheck == 6:   #가장 등장횟수가 많은 번호가 6번일 때
    while check[6]-check[9] >= 2:   #6과 9가 2 이상 차이나면
        check[6] -= 1   #6에서 9에게 1 나눠줌
        check[9] += 1   #9는 6에게서 1 받음
elif maxCheck == 9: #9도 6과 동일한 메커니즘
    while check[9]-check[6] >= 2:
        check[9] -= 1
        check[6] += 1
maxCheck = max(check, key=check.get)    #최종적으로 가장 큰 value를 가진 key 찾아내기
print(check[maxCheck])  #해당 key의 등장횟수만큼 초의 세트를 사용하게 됨