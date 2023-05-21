from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    charge = []
    car_w = []
    for _ in range(n):
        charge.append(int(input()))
    for _ in range(m):
        car_w.append(int(input()))

    parking = [0 for _ in range(n)]
    parking_car = 0 #현재 주차된 차의 수
    queue = deque() #대기장소
    total = 0
    dic = {i:-1 for i in range(m+1)}    #차량별 현재 주차된 위치
    arr = []
    for _ in range(2*m):
        arr.append(int(input()))

    for i in arr:
        while parking_car < n and queue:  # 주차공간 여유있으면
            a = queue.popleft()
            for j in range(n):
                if parking[j] == 0:
                    parking[j] = 1
                    dic[a] = j
                    total += car_w[a - 1] * charge[j]
                    parking_car += 1
                    break
        if i >= 0:   #입차
            queue.append(i)  # 대기 시키기
        else:
            parking[dic[abs(i)]] = 0  # 주차공간 비워주기
            dic[abs(i)] = -1
            parking_car -= 1
    print("#{} {}".format(test_case, total))