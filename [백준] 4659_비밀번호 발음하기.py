import sys
input=sys.stdin.readline
alphabet_list = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
mo = set(["a", "e", "i", "o", "u"]) #알파벳 모음
ja = alphabet_list - mo #알파벳 자음(모든 알파벳-알파벳 모음)
while True:
    ans = " is not acceptable." #ans값 초기화
    c = input().rstrip()
    a = list(c)
    if c == "end":  #입력받은 값이 "end"이면 while문 종료
        break
    flag = 0    #모음이 사용됐는지 체크하는 플래그
    for i in range(len(a)): #입력받은 문자열을 순차적으로 돌며 조건에 부합하는지 확인
        if a[i] in mo:  #모음 중 하나를 사용했다면
            flag = 1    #flag를 1로 설정
        if i < len(a)-2:    #out of index 에러 방지
            #연이은 3개의 문자가 모두 모음에 속하거나 자음에 속한다면 for문 종료
            if (a[i] in mo and a[i+1] in mo and a[i+2] in mo) or (a[i] in ja and a[i+1] in ja and a[i+2] in ja):
                break
        if i < len(a) - 1:
            #연이은 문자 2개가 동일하고, 두 문자가 e나 o가 아닌 경우 for문 종료
            if a[i] == a[i+1] and (a[i] != "e" and a[i] != "o"):
                break
    else:   #중간에 break문이 실행되지 않았다면
        if flag:    #문자열에 모음이 포함되었다면
            ans = " is acceptable." #ans값 변경
    print("<"+c+">"+ans)






