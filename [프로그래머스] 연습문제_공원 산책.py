from collections import deque
def solution(park, routes):
    answer = [0, 0]
    n = len(park)   #세로
    m = len(park[0])    #가로
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                answer[0] = i   #y축
                answer[1] = j   #x축
    for k in routes:
        a, b = k.split()
        b = int(b)
        flag = False
        if a == "E":    #동쪽으로(x축)
            if answer[1]+b >= m:
                continue
            for i in range(1, b+1):
                if park[answer[0]][answer[1]+i] == "X":
                    flag = True
                    break
            if flag == True:
                continue
            answer[1] += b
        elif a == "W":  #서쪽으로(x축)
            if answer[1]-b < 0:
                continue
            for i in range(1, b+1):
                if park[answer[0]][answer[1]-i] == "X":
                    flag = True
                    break
            if flag == True:
                continue
            answer[1] -= b
        elif a == "S":  #남쪽으로(y축)
            if answer[0]+b >= n:
                continue
            for i in range(1, b+1):
                if park[answer[0]+i][answer[1]] == "X":
                    flag = True
                    break
            if flag == True:
                continue
            answer[0] += b
        elif a == "N":  #북쪽으로(y축)
            if answer[0]-b < 0:
                continue
            for i in range(1, b+1):
                if park[answer[0]-i][answer[1]] == "X":
                    flag = True
                    break
            if flag == True:
                continue
            answer[0] -= b
    return answer