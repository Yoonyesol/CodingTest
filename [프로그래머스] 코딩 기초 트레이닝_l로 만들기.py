def solution(myString):
    answer = ''
    for alpha in myString:
        if ord(alpha) < 108:
            answer += 'l'
        else:
            answer += alpha
    return answer