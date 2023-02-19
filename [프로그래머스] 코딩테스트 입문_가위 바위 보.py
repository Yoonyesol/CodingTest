def solution(rsp):
    dic = {"2":"0", "0":"5", "5":"2"}
    answer = ''
    for i in rsp:
        answer += dic[i]
    return answer