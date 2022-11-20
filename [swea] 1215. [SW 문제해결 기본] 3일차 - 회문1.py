T = 10
for test_case in range(1, T + 1):
    test_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    ans = [0] * 4	#[max(행의 합), max(열의 합), 대각선1, 대각선2]
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            if i == j:	#왼쪽 끝에서 시작하는 대각선
                ans[2] += arr[i][j]
            if i + j == 99:	#오른쪽 끝에서 시작하는 대각선
                ans[3] += arr[i][j]
        if ans[0] < row_sum:	#기존 행 값보다 더 큰 값이 들어오면
            ans[0] = row_sum	#값을 변경
        if ans[1] < col_sum:
            ans[1] = col_sum
    print("#{} {}".format(test_case, max(ans)))