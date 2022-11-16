T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    data = list(map(int, input().split()))
    i = 1
    while True:
        if i > 5:
            i = 1
        data.append(data.pop(0)-i)
        if data[7] <= 0:
            data[7] = 0
            break
        i += 1
    print("#{} {} {} {} {} {} {} {} {}".format(tc, *data))