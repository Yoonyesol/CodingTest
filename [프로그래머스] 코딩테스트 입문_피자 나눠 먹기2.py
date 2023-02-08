def solution(n):
    result = n
    i = 2
    while True:
        if result % 6 == 0:
            break
        result = n * i
        i+=1
    return result // 6