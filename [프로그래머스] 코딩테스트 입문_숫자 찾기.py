def solution(num, k):
    num = list(map(int, str(num)))
    return num.index(k)+1 if k in num else -1