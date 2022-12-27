def solution(t, p):
    answer, num, i = 0, 0, 0
    while True:
        if i+len(p) > len(t):   #out of index 방지
            break
        num = int(t[i:i+len(p)])    #p의 길이만큼 문자열 슬라이싱
        if num <= int(p):
            answer += 1
        i += 1
    return answer