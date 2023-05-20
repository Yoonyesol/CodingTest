T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    cnt = n
    num = 1
    i, j = 0, 0
    while cnt:
        for _ in range(cnt):
            arr[i][j] = num
            j += 1
            num += 1
        j -= 1
        i += 1
        cnt -= 1
        if cnt == 0: break
        for _ in range(cnt):
            arr[i][j] = num
            i += 1
            num += 1
        j -= 1
        i -= 1
        for _ in range(cnt):
            arr[i][j] = num
            j -= 1
            num += 1
        cnt -= 1
        if cnt == 0: break
        i -= 1
        j += 1
        for _ in range(cnt):
            arr[i][j] = num
            i -= 1
            num += 1
        j += 1
        i += 1
    print("#{}".format(test_case))
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()