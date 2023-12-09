import sys
input = sys.stdin.readline

chulsu = [list(map(int, input().split())) for _ in range(5)]    #철수의 빙고판
indexList = dict()  #철수의 빙고판 내부 숫자(key)와 인덱스(value)를 저장하는 인덱스딕셔너리 

for i in range(5):
    for j in range(5):
        indexList[chulsu[i][j]] = (i, j)    #철수 빙고판 숫자: 인덱스 저장

bingoList = [[] for _ in range(12)] #가로5, 세로5, 대각선2의 체크된 인덱스를 저장하는 리스트
num = 0 #사회자가 부른 숫자 수 카운트하는 변수
flag = False    #빙고가 완성됐는지 체크하는 플래그
ans = [list(map(int, input().split())) for _ in range(5)]   #사회자가 부른 번호

for i in range(5):
    for j in range(5):
        num += 1    #사회자 호명 번호 개수 카운팅
        cnt = 0 #가로 or 세로 or 대각선 중 다 채운 항목이 있는지 체크하는 변수
        bingoList[indexList[ans[i][j]][0]].append(indexList[ans[i][j]]) #사회자가 부른 수가 철수 빙고판의 어떤 인덱스에 있는지 확인하고, 해당 인덱스의 가로 리스트에 해당 인덱스 저장
        bingoList[indexList[ans[i][j]][1]+5].append(indexList[ans[i][j]]) #사회자가 부른 수가 철수 빙고판의 어떤 인덱스에 있는지 확인하고, 해당 인덱스의 세로 리스트에 해당 인덱스 저장
        if indexList[ans[i][j]][0] == indexList[ans[i][j]][1]:  #왼->오 대각선 확인
            bingoList[10].append(indexList[ans[i][j]])
        if indexList[ans[i][j]][0] + indexList[ans[i][j]][1] == 4:  #오->왼 대각선 확인
            bingoList[11].append(indexList[ans[i][j]])

        for k in range(len(bingoList)): #채워진 리스트 중 빙고가 몇 개 있는지 카운팅
            if len(bingoList[k]) >= 5:  #5개 이상 채워지면 1빙고
                cnt += 1

        if cnt >= 3:    #3개 이상 빙고가 나온다면
            flag = True #게임 종료 플래그
            print(num)  #사회자 호명 횟수 출력
            break   #for문 탈출

    if flag:    #게임 종료 플래그가 세워졌을 시
        break   #가장 외부에 있는 for문 탈출