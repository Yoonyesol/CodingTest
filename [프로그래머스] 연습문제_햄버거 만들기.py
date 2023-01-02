def solution(ingredient):
    answer = 0
    s = []
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:  #인덱스 -4에서부터 끝까지
            answer += 1
            for _ in range(4):  #s 가장 뒤 원소 pop 4번 반복(1, 2, 3, 1 제거)
                s.pop()
    return answer