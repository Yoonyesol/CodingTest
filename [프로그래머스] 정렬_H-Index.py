def solution(citations):
    answer = 0
    citations.sort()
    for i in range(1, len(citations)+1):
        hindex = citations[-i]
        if hindex >= i:
            answer = i
    return answer