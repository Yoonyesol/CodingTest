def solution(s):
    answer = 1  #문자열 분리 전 하나의 단어
    x = s[0]
    same = 0
    diff = 0
    for i in range(len(s)):
        if s[i] == x:   #첫글자와 동일할 경우
            same += 1
        elif s[i] != x: #첫글자와 다를 경우
            diff += 1
        if same and (same == diff): #same이 1이상이고 same과 diff값이 동일할 때
            if i < len(s)-1:    #i가 index out of range되지 않게 조절
                x = s[i + 1]    #다음 x 선정
                same = 0
                diff = 0
                answer += 1 #문자열 분리 카운트
    return answer