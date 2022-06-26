def solution(s):
    answer = s.split()
    al = list(map(int, answer))
    return str(min(al)) + " " + str(max(al))