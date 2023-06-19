def solution(code):
    ret = ''    #반환할 문자열
    mode = 0    #모드(초기값 0)
    for idx in range(len(code)):
        if mode == 1:   #모드가 1일 때
            if code[idx] == "1":    #문자가 "1"이면
                mode = 0    #모드를 0으로 바꾼다.
            else:   #문자가 "1"이 아니면
                if idx % 2 != 0:    #idx가 홀수일 때만
                    ret += code[idx]    #ret의 맨 뒤에 code[idx]를 추가
        elif mode == 0:   #모드가 0일 때
            if code[idx] == "1":    #문자가 "1"이면
                mode = 1    #모드를 1로 바꾼다.
            else:   #문자가 "1"이 아니면
                if idx % 2 == 0:    #idx가 짝수일 때만
                    ret += code[idx]    #ret의 맨 뒤에 code[idx]를 추가
    if ret == "": return "EMPTY"    #return하려는 ret가 빈 문자열이라면 "EMPTY" return
    else: return ret    #빈문자열 아니라면 ret return