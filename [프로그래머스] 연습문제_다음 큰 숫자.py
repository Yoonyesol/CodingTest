def solution(n):
    answer = format(n, "b").count("1")
    for i in range(n+1, 1000001):
        answer2 = format(i, "b").count("1")
        if answer == answer2:
            return i