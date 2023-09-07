import sys
from collections import deque
input = sys.stdin.readline
arr = [deque(str(input()).rstrip()) for i in range(4)]  #rotate() 사용하기 위해 deque로 배열 저장
k = int(input())    #회전 횟수
for _ in range(k):
    a, b = map(int, input().split())    #톱니바퀴 번호, 방향
    a -= 1  #인덱스와 맞추기 위해 -1 (1번 톱니바퀴 == arr 0번 인덱스)
    i = 0
    b_copy = b #b 복사본
    rotate = {1:[], -1:[]}  #key:돌아가는 방향, value:key방향으로 돌아갈 톱니바퀴 리스트
    while a - i -1 >= 0:   #왼쪽 톱니바퀴 확인
        if arr[a-i-1][2] != arr[a-i][6]:    #맞물리는 부분의 극이 다를 때
            b_copy = -(b_copy) #현재(오른쪽) b_copy와 반대 방향으로 돌아가도록
            rotate[b_copy].append(a-i-1)    #회전 방향을 키로 하는 리스트에 왼쪽 톱니바퀴 추가
        else:   #맞물리는 부분의 극이 같다면 그 이전의 톱니바퀴들은 더 이상 확인할 필요 없다(극이 다를 때만 회전하고, 왼쪽 톱니가 회전하지 않으면 그 왼쪽의 톱니도 회전하지 않음.)
            break
        i += 1  #i+1을 하며 a 이전의 톱니바퀴들까지 확인
    i = 0
    b_copy = b
    while a + i + 1 <= 3:   #오른쪽 톱니바퀴 확인. 로직은 위의 while과 동일
        if arr[a+i+1][6] != arr[a+i][2]:
            b_copy = -(b_copy)
            rotate[b_copy].append(a+i+1)
        else:
            break
        i += 1
    arr[a].rotate(b)    #a를 b만큼 회전시킨다.
    for i in rotate[-1]:    #왼쪽으로 이동할 목록의 톱니들을 왼쪽으로 회전
        arr[i].rotate(-1)
    for i in rotate[1]: #오른쪽으로 회전
        arr[i].rotate(1)
#12시 방향의 극의 점수의 합
print(int(arr[0][0]) * 1 + int(arr[1][0]) * 2 + int(arr[2][0]) * 4 + int(arr[3][0]) * 8)