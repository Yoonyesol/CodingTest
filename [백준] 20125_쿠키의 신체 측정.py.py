import sys
input=sys.stdin.readline

n = int(input().rstrip())
arr = [list(input().rstrip()) for _ in range(n)]
waist = []  #허리 좌표
heart_position = (0, 0) #심장 좌표
l_arm, r_arm = 0, 0 #왼팔 오른팔 길이
l_leg, r_leg = 0, 0 #왼다리 오른다리 길이

for i in range(n):
    arrCnt = arr[i].count("*")  #한 행에 *이 몇 개 있는지 확인
    for j in range(n):
        if arr[i][j] == "*":    #*이 나올 경우
            if arrCnt == 1 and r_leg == 0 and l_leg == 0:   #한 행에 *이 하나밖에 없고 다리 두개 길이가 0이면 == 허리 위
                if arr[i+1][j] == "*":  #아래에 "*"이 있고 == 허리or머리
                    if heart_position == (0,0): #심장이 아직 없으면 == 머리
                        heart_position = (i+1, j)   #심장 좌표 저장
                        continue    #아래 문장 실행하지 않게 건너뛰기
                waist.append((i, j))    #한 행에 *이 하나밖에 없고 머리가 아니면 => 허리 좌표 저장
                continue    #아래 코드 실행하지 않고 건너뜀

            if arrCnt >= 3: #한 행에 *이 3개 이상인 경우 왼팔, 심장, 오른팔
                if heart_position[1] > j:   #심장 위치의 왼쪽 열
                    l_arm += 1
                elif heart_position[1] < j: #심장 위치의 오른쪽 열
                    r_arm += 1
                continue

            if waist and i > waist[-1][0]:    #허리 좌표가 존재하면서 행이 허리 아래
                if j > waist[-1][1]:    #가장 마지막 허리의 오른쪽 열
                    r_leg += 1
                elif j < waist[-1][1]:  #가장 마지막 허리의 왼쪽 열
                    l_leg += 1

print(heart_position[0]+1, heart_position[1]+1) #심장 좌표. 시작 좌표가 1,1이므로 행열에 1씩 더해주기
print(l_arm, r_arm, len(waist), l_leg, r_leg)   #왼오른팔, 허리, 왼오른다리 길이