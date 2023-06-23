import sys
input=sys.stdin.readline
p, m = map(int, input().split())    #p:플레이어의 수, m:방의 정원
arr = []    #플레이어 레벨, 닉네임을 저장할 배열
for i in range(p):
    arr.append(list(input().split()))   #이차원 배열로 [레벨, 닉네임] 저장
room = []   #랭킹전 열리는 방
for i, j in arr:
    if len(room) == 0:  #개설된 방이 없다면
        room.append([[i, j]])   #방 개설
    else:   #개설된 방이 있다면
        for k in range(len(room)):  #모든 방을 살핀다
            if len(room[k]) == m:   #풀방
                continue
            # 풀방이 아니라면, 방에 가장 처음 들어온 사람의 레벨과 +-10 차이가 나는지 확인
            if int(room[k][0][0]) - 10 <= int(i) <= int(room[k][0][0]) + 10:
                room[k].append([i, j])  #방에 입장
                break   #다른 방에 중복해서 들어갈 수 없도록 for문 벗어남
        else:   #중간에 break에 걸리지 않았다면, 들어갈 수 있는 방이 없는 것이므로 새롭게 방을 개설
            room.append([[i, j]])

#모든 플레이어를 방에 집어넣고 최종적으로 모든 방 확인
for i in room:
    if len(i) == m: #풀방=>게임시작
        print("Started!")
    else:   #풀방x=>인원대기
        print("Waiting!")
    #플레이어 닉네임을 기준으로 각 방의 인원을 정렬
    sorted_i = sorted(i, key=lambda x:x[1])
    for j in sorted_i:  #정렬한 각 방의 인원의 레벨, 닉네임 출력
        print(' '.join(j))