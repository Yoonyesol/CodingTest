import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medal = [list(map(int, input().split())) for _ in range(n)]

#금은동 중요도 순으로 입력받은 내용 정렬
medal = sorted(medal, key=lambda x: (-x[1], -x[2], -x[3]))

ranking = {}    #팀:등수 저장할 딕셔너리
rank = 1    #실제 등수 체크
tmp = 1 #동일 등수일 시 +1씩 늘려 rank에 반영할 변수

for i in range(n):
    if medal[i][0] not in ranking.keys():   #ranking 딕셔너리에 key가 존재하지 않는다면,
        ranking[medal[i][0]] = rank #새롭게 key와 value를 지정
    # out of range오류 해결을 위해 i < n-1 조건 붙여주기. 앞의 메달 수와 뒤의 메달 수를 비교해 모두 같으면 같은 등수
    if i < n-1 and medal[i][1] == medal[i+1][1] and medal[i][2] == medal[i+1][2] and medal[i][3] == medal[i+1][3]:
        ranking[medal[i+1][0]] = rank   #다음 팀도 동일한 rank 저장
        tmp += 1    #등수 건너뛰기 위한 tmp 1늘림
    else:   #동일하지 않을 시
        rank += tmp #이전까지의 동일등수에서 늘려놨던 tmp를 rank에 더해서 rank업데이트
        tmp = 1 #초기화

print(ranking[k])   #원하는 팀의 등수 출력

