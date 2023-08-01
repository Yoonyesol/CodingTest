import sys
input=sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    a = list(input().rstrip())  #문장을 입력받기
    str = ''    #숫자 문자를 저장할 변수 초기화
    for i in a: #문장의 한 글자씩 확인
        if i.isdigit(): #각 문자가 숫자인지 확인
            str += i    #해당 문자가 숫자인 한, 계속 str에 문자열을 붙여 저장
        else:   #문자가 숫자가 아닌 경우
            if str != '':   #str에 저장된 값이 존재한다면(해당 코드 작성x시, int('')에러 발생)
                arr.append(int(str))    #해당 값을 숫자로 바꾸어 arr 배열에 저장
                str = ''    #다음 숫자를 저장하기 위해 str을 초기화
    if str != '':   #마지막 글자가 숫자인 경우를 처리하기 위해 해당 코드 작성
        arr.append(int(str))
for i in sorted(arr):   #오름차순 정렬한 리스트의 원소를 순서대로 출력
    print(i)