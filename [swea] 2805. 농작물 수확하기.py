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


--------------------------------

23/05/08

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())    #농장의 크기
    values = []
    ans = 0
    n_sum = 0
    for i in range(n):
        col = list(map(int, input().rstrip()))
        n_sum += sum(col)
        values.append(col)
    for i in range(n):
        if i < (n // 2):
            n_sum -= sum(values[i][:n//2-i])
            n_sum -= sum(values[i][-(n//2-i):])
        elif i > (n // 2):
            n_sum -= sum(values[i][:-(n//2-i)])
            n_sum -= sum(values[i][(n//2-i):])
    print("#{} {}".format(test_case, n_sum))