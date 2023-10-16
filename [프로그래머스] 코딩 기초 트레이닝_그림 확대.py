def solution(picture, k):
    answer = []
    for i in picture:
        p = ''
        for j in i:
            p += j*k
        for _ in range(k):
            answer.append(p)
    return answer