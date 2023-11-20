T = int(input())
for test_case in range(1, T + 1):
    n = int(input().rstrip())
    wires = []	#이전 전선 저장하는 리스트
    cnt = 0	#교차점 개수 카운팅하는 변수

    for _ in range(n):
        a, b = map(int, input().split())    #시작, 끝
        if wires:	#리스트가 비어있지 않다면
            for i, j in wires:  #시작, 끝
                if (i > a and j < b) or (a > i and b < j):	#교차 상태
                    cnt += 1	#교차점 개수 늘리기
        wires.append((a, b))	#이전 전선들과 비교한 전선을 리스트에 새로 저장

    print(f'#{test_case} {cnt}')