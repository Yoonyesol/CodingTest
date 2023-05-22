def trans(num, base):
    r = ''
    numbers = "0123456789ABCDEF"
    if num == 0:    #num이 0인 경우는 while문 돌지 않으므로 따로 처리해줌
        return "0"
    while num:
        r = numbers[num%base]+r #이전에 변환한 r이 맨 뒤로 가게 처리
        num //= base
    return r

def solution(n, t, m, p):
    answer = ''
    txt = ''
    for i in range(t*m):    #전체길이=튜브가 말할 숫자*인원수
        txt += trans(i, n)  #0부터 t*m까지 n진법 변환
    
    for i in range(p-1, t*m, m):  #튜브의 순서부터 m개씩 건너뛰기
        answer += txt[i]
    return answer