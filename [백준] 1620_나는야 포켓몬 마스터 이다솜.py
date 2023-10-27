import sys
input=sys.stdin.readline
n, m = map(int, input().split())

dic1 = dict()   #key: number, value: alpha
dic2 = dict()   #key: alpha, value: number

#입력받은 포켓몬을 도감에 입력
for i in range(n):
    monster = input().rstrip()
    dic1[str(i+1)] = monster    #문자열 숫자를 key로 사용해 도감에 저장
    dic2[monster] = str(i+1)    #포켓몬을 key로 문자열 숫자를 저장

for i in range(m):
    question = input().rstrip()
    if question.isalpha():  #입력받은 수가 알파벳이라면
        print(dic2[question])   #dic2에서 알파벳을 key로 값을 구한다.
    else:   #입력받은 수가 숫자라면
        print(dic1[question])   #dic1에서 숫자를 key로 값을 구한다.

#깨달은 점: 숫자 문자열도 isalpha()가 정상적으로 동작한다.
#추가
#value로 key를 찾기: [k for k, v in aa.items() if v == 'CC'] -> 딕셔너리 전체를 순회하므로 비효율적
#전체 dictionary가 주어진 경우, key:val을 val:key로 뒤집어 새로운 dict를 생성해 원하는 데이터를 찾을 수도 있다.
#bb = {v:k for k,v in aa.items()} #// {'AA': '0', 'BB': '1', 'CC': '2'}
#아래와 같이 for문을 이용해서 값을 구할 수도 있다. 
# for key, value in dict.items():
#     if value == '35':
#         print(key)
