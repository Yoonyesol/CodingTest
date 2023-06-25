import sys
input=sys.stdin.readline
n = int(input())
i = 665 #1씩 늘려가며 원하는 수를 찾기위한 변수
cnt = 0 #몇번째 지구종말 수인지 카운트
while True:
    i += 1  #1씩 늘려가며
    if '666' in str(i): #i에 666이 포함되어 있으면 카운팅
        cnt += 1
    if cnt == n:    #n번째로 큰 지구종말 수 
        print(i)    #해당 수를 출력한다.
        break