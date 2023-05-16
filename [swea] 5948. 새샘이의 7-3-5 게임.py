T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    ans = 0
    ans_set = set()
    for i in range(7):
        for j in range(7):
            for k in range(7):
                if i != j and j != k and k != i:
                    ans_set.add(arr[i] + arr[j] + arr[k])
    print("#{} {}".format(test_case, sorted(ans_set)[-5]))