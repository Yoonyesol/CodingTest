T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    avg = sum(arr)//n
    cnt = 0
    for i in arr:
        if i <= avg:
            cnt+=1
    print("#{} {}".format(test_case, cnt))