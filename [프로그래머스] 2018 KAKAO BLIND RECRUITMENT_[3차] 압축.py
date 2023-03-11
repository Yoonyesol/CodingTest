def solution(msg):
    answer = []
    dic = {chr(i+ord("A")-1):i for i in range(1, 27)}
    idx = 27
    checkMsg = ""
    for i in msg:
        checkMsg += i
        if checkMsg not in dic:
            answer.append(dic[checkMsg[:-1]])
            dic[checkMsg] = idx
            idx += 1
            checkMsg = checkMsg[-1]
    answer.append(dic[checkMsg])
    return answer