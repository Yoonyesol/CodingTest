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


-----------------------------------


T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    arr = [i for i in list(map(int, input().split()))]
    i = 1
    while True:
        a = arr.pop(0)-i
        if a <= 0:
            arr.append(0)
            break
        else:
            arr.append(a)
        i += 1
        if i > 5:
            i = 1
    print("#{} {}".format(test_case, ' '.join(map(str, arr))))