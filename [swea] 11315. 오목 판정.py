def search(arr):
    dx = [1, 0, 1, 1]
    dy = [0, 1, -1, 1]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "o":
                for k in range(4):
                    x = i
                    y = j
                    cnt = 0
                    while 0 <= x <= n-1 and 0 <= y <= n-1 and arr[x][y]=="o":
                        cnt += 1
                        x += dx[k]
                        y += dy[k]
                        if cnt == 5:
                            return "YES"
    return "NO"
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())
    print("#{} {}".format(test_case, search(arr)))