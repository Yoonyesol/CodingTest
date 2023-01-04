def solution(priorities, location):
    answer = 0
    pri = [(element, idx) for (idx, element) in enumerate(priorities)]  #[(원소, 인덱스), (원소, 인덱스),...]
    while True:
        if pri[0][0] == max(pri)[0]:    #가장 처음 원소값이 max와 같다면(max는 튜플의 첫번째 원소 기준으로 실행됨)
            answer += 1 #몇번째에 location원소가 존재하는지 체크
            if pri[0][1] == location:   #가장 처음 인덱스 값이 location과 같아질 때 종료
                break
            pri.pop(0)  #가장 처음 인덱스 값이 location과 같아질 때까지 앞의 원소를 pop해서 없앰
        else:
            pri.append(pri.pop(0))  #목록 중에 처음 원소보다 큰 값이 존재하면 가장 앞 원소를 맨 뒤로 append
    return answer