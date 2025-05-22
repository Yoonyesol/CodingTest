import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0 #그룹단어 체크하는 변수
for _ in range(n):
    a = input().rstrip()    #입력받은 문장
    list = []   #체크한 문자열 저장
    for i in a: #입력받은 단어 한 글자씩 확인
        if not list:    #리스트의 길이가 0이면 일단 한글자 넣음
            list.append(i)
            continue
        if list[-1] != i:   #리스트 마지막 글자가 새로 확인할 글자와 다르면
            if i in list:   #기존 리스트에 새로 확인할 글자가 존재하는지 확인
                break   #존재한다면 for문 탈출
            list.append(i)  #존재하지 않는다면 해당 글자를 리스트 안에 넣어서 체크표시
    else:   #for문 중간에 탈출이 일어나지 않으면, 그룹단어라는 뜻
        cnt += 1    #그룹단어 갯수 체크
print(cnt)

#-----------
#25.05.22
n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

cnt = 0
for i in arr:   #arr 내부 단어 하나씩 체크
    stack = []
    for j in range(len(i)): #단어 char 인덱스 j
        if len(stack) == 0:
            stack.append(i[j])
            continue
        if i[j] != stack[-1] and i[j] in stack:
            break
        stack.append(i[j])
    else:
        cnt += 1
print(cnt)