def solution(n, m, section):
    answer = 0
    while section:
        e = section[0]
        while section and e <= section[0] < e+m:
            section.pop(0)
        answer+=1    
    return answer