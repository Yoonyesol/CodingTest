import sys
input = sys.stdin.readline

tc = int(input().rstrip())
for _ in range(tc):
    n, k, t, m = map(int, input().split())      #팀개수, 문제 개수, 구해야 할 팀 id, 로그개수
    dic = {i: [[0 for _ in range(k+1)], 0, 0] for i in range(1, n+1)}   #팀id: 문제별 점수리스트, 시도횟수, 마지막 제출 시간
    for idx in range(m):    #전체 로그 개수(m)번 반복
        i, j, s = map(int, input().split()) #팀id, 문제번호, 점수
        dic[i][0][j] = max(dic[i][0][j], s) #문제 인덱스의 점수를 둘 중 더 큰 수로 업데이트
        dic[i][1] += 1  #시도횟수 증가
        dic[i][2] = idx #마지막 제출 시간 업데이트

    dic = sorted(dic.items(), key=lambda x:(-sum(x[1][0]), x[1][1], x[1][2]))   #문제 전체 합계 내림차순, 풀이 시도횟수/제출시간 오름차순 정렬

    for i in range(len(dic)):   #전체 dic을 돌면서
        if t == dic[i][0]:  #구해야 할 id와 key 값이 동일하다면
            print(i+1)  #등수 출력(인덱스+1)
            break
