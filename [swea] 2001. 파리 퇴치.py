tc = int(input())

for t in range(1, tc+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_val = 0

    #전체 배열 탐색
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0    #파리채 내리친 곳의 파리개수
            #파리채로 내리칠 곳의 파리 개수 탐색
            for k in range(m):
                for l in range(m):
                    temp += arr[i+k][j+l]
            if max_val < temp:
                max_val = temp

    print("#{} {}".format(t, max_val))