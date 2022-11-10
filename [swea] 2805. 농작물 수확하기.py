T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    worth = [list(map(int, input())) for _ in range(N)]
    sum = 0
    mid = N // 2
    start = mid
    end = mid
    for i in range(N):
        for j in range(start, end+1):
            sum += worth[i][j]
        if i < mid:	#상단(중간보다 위쪽), 증가
            start-=1
            end+=1
        else:	#하단(중간+중간보다 아래쪽), 감소
            start+=1
            end-=1
    print("#{} {}".format(test_case, sum))