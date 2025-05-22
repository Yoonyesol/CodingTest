import sys
input=sys.stdin.readline
n = int(input())    #스위치의 개수
arr = [i for i in map(int, input().split())]    #스위치 초기상태
turn = int(input()) #몇번의 turn이 주어지는지 입력받기
for _ in range(turn):   #turn의 수만큼 스위치 켜고 끄기 반복
    gender, idx = map(int, input().split())    #gender:성별, b:받은 스위치 번호(실제 인덱스 구할 때는 -1)
    if gender == 1:  #남학생
        for i in range(idx-1, len(arr), idx):   #현재 인덱스부터 끝 인덱스까지, 매번 idx만큼 뛰어 idx배의 인덱스 원소만 순회하며 스위치 바꾸기
            if arr[i] == 1: #1인 경우
                arr[i] = 0  #0으로 바꿈
            else:
                arr[i] = 1
    elif gender == 2:    #여학생
        idx1, idx2 = idx-1, idx-1   #확인해야 할 왼쪽 인덱스, 오른쪽 인덱스. 처음에는 부여받은 인덱스번호로 초기화
        if arr[idx-1] == 1: #현재 인덱스번호의 스위치를 바꾸기
            arr[idx-1] = 0
        else:
            arr[idx-1] = 1
        while True: #조건에 부합할 때까지 왼쪽인덱스, 오른쪽 인덱스 탐색
            idx1 -= 1   #인덱스를 현재 위치에서 왼쪽으로 이동
            idx2 += 1   #인덱스를 현재 위치에서 오른쪽으로 이동
            if idx1 < 0 or idx2 > len(arr)-1:   #배열의 범위를 벗어난 경우 처리
                break   #이 경우 왼쪽 인덱스의 값과 오른쪽 인덱스의 값이 존재하지 않으므로 동일한 값을 가질 수 없기 때문에 그냥 반복문을 종료시켜버린다
            if arr[idx1] != arr[idx2]:  #왼쪽 인덱스의 값과 오른쪽 인덱스의 값이 동일하지 않으면 더이상 순회할 필요가 없으므로 반복문을 종료시킨다.
                break
            if arr[idx1] == 1:  #위의 사항에 해당되지 않는 경우는 왼쪽 인덱스의 값과 오른쪽 인덱스의 값이 동일하다는 뜻이므로 스위치를 바꿔준다.
                arr[idx1] = 0
                arr[idx2] = 0
            else:
                arr[idx1] = 1
                arr[idx2] = 1
cnt = 0 #현재 화면에 찍은 문자의 개수를 카운팅하는 변수
for i in arr:
    print(i, end=" ")   #매번 띄어쓰기를 하여 배열의 원소를 출력
    cnt += 1    #화면에 찍은 문자 개수 카운팅
    if cnt == 20:   #문자를 20개 찍었다면
        print() #줄바꿈
        cnt = 0 #cnt값 초기화

#-----------------------
# 25.05.23
s_num = int(input())
s_stat = list(map(int, input().split()))
student = int(input())

for _ in range(student):
    gender, b = map(int, input().split())
    if gender == 1: #남학생
        for i in range(b-1, len(s_stat), b):
            if s_stat[i] == 1:
                s_stat[i] = 0
            else:
                s_stat[i] = 1
    elif gender == 2:   #여학생
        if s_stat[b-1] == 1:
            s_stat[b-1] = 0
        else:
            s_stat[b-1] = 1
        x, y = b - 1, b - 1
        while True:
            x -= 1
            y += 1
            if x < 0 or y >= len(s_stat):
                break
            if s_stat[x] != s_stat[y]:
                break
            if s_stat[x] == 1:
                s_stat[x] = 0
                s_stat[y] = 0
            elif s_stat[x] == 0:
                s_stat[x] = 1
                s_stat[y] = 1

cnt = 0
for i in s_stat:
    print(i, end=" ")
    cnt += 1
    if cnt == 20:
        print()
        cnt = 0