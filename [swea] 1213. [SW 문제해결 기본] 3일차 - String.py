T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    fstring = input()
    cnt = 0
    estring = input()
    while estring.find(fstring) != -1:	#문자열을 찾을 수 없을 때까지 탐색
        cnt += 1
        estring = estring[estring.find(fstring) + len(fstring):]	#찾은 문자열까지 estring에서 슬라이싱하여 지우기
    print("#{} {}".format(test_case, cnt))