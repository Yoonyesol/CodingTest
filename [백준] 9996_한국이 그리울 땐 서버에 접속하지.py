import sys
input=sys.stdin.readline
n = int(input())
pattern = input().rstrip()
pattern_len = len(pattern)-1    #"*"을 제외한 패턴의 총 길이
pattern = pattern.split("*")    #"*"을 기준으로 문자열을 잘라 리스트에 저장
for i in range(n):
    ans = "NE"
    f_name = input().rstrip()
    if len(f_name) < pattern_len:   #입력받은 문자열이 패턴보다 짧은 경우 아래 코드를 진행하지 않고 "ans" 출력후 종료
        print(ans)
        continue
    if f_name[:len(pattern[0])] == pattern[0]:  #패턴의 길이에 맞추어 문자열의 앞과 뒤를 비교
        if f_name[len(pattern[1])*-1:] == pattern[1]:
            ans = "DA"
    print(ans)
