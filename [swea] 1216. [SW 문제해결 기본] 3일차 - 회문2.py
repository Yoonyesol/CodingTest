for test_case in range(1, 11):
    int(input())
    arr = []
    max_len = 0
    for _ in range(100):
        arr.append(list(input()))
    for i in range(100):
        b = ''
        for j in range(100):
            for k in range(100-j+1):
                if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                    max_len = max(max_len, k)
            b += arr[j][i]
        for m in range(100):
            for n in range(100-m+1):
                if b[m:m+n] == b[m:m+n][::-1]:
                    max_len = max(max_len, n)
    print("#{} {}".format(test_case, max_len))