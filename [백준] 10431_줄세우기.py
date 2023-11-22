import sys
input = sys.stdin.readline

tc = int(input().rstrip())
for _ in range(tc):
    students = list(map(int, input().split()))
    tcNum = students[0] #테케 넘버
    students = students[1:] #학생들 키 리스트
    newArr = [] #줄 세우기 위한 빈 리스트
    maxStu = 0  #가장 키가 큰 학생의 키
    cnt = 0 #뒤로 물러나는 횟수 카운팅

    for i in range(len(students)):
        if i == 0:  #처음에는 아무나 골라서
            newArr.append(students[i])  #가장 앞에 세운다.
            maxStu = students[i]    #현재 학생이 가장 키 큰 학생
            continue    #아래 코드 실행 건너뛰기
        if maxStu <= students[i]:   #자기 앞 학생 중 키 큰 학생이 없을 시
            newArr.append(students[i])  #가장 뒤에 선다.
            maxStu = students[i]    #내가 가장 키 큼
        else:   #내 앞에 나보다 키가 크거나 동일한 키의 사람이 있다면
            for j in range(len(newArr)):    #새로 줄 서 있는 리스트 순회하기
                if newArr[j] >= students[i]:    #나보다 키 큰 가장 첫번째 학생의 인덱스 찾기
                    cnt += len(newArr)-j    #물러나는 횟수(내가 끼어드는 만큼 나보다 키큰 애들은 뒤로 물러나야 함)
                    newArr.insert(j, students[i])   #해당 자리에 끼어들기
                    break   #반복문 종료

    print(f'{tcNum} {cnt}')