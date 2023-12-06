import sys
input = sys.stdin.readline

arr = list(input().rstrip())
reform = '' #문자를 저장해 새로 만들 문자열
flag = False    #괄호 안인지 아닌지 확인하는 플래그
tmp = ''    #문자열 뒤집기 위한 문자열 저장 임시공간

for i in range(len(arr)):   #전체 문자열 순회
    if arr[i] == "<":   #괄호 시작 시 플래그 True로 만들기
        flag = True
        reform += tmp[::-1] #기존에 저장돼 있던 tmp값을 뒤집어서 reform에 저장
        tmp = ''    #저장한 값은 비우기
    elif arr[i] == ">": #괄호 닫히면 플래그 False로 만들기
        flag = False

    if flag:    #괄호내부라면, 뒤집기 없이 그냥 저장
        reform += arr[i]
    else:   #괄호 외부라면
        if arr[i] == " ":   #공백이 주어질 시
            reform += tmp[::-1] #이전까지 저장한 tmp값을 reform에 뒤집어서 저장
            reform += arr[i]   #이번에 받은 공백을 reform에 추가
            tmp = ''    #tmp 비우기
        elif i == len(arr)-1:   #문자열 마지막일 때
            tmp += arr[i]   #마지막 문자열까지 안에 넣고
            reform += tmp[::-1] #tmp값을 뒤집어서 reform에 추가
        elif arr[i] == ">": #닫힌 괄호일 시
            reform += arr[i]    #뒤집기에 포함시키지 않고 reform에 바로 넣어준다
        else:   #위의 모든 사항에 해당하지 않을 시
            tmp += arr[i]   #그냥 tmp에 문자를 추가한다
print(reform)