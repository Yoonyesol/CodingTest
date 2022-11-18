T = int(input())
for test_case in range(1, T + 1):
    ans = "Possible"
    N, M, K = map(int, input().split())	#N명, M초, K개
    people = list(map(int, input().split()))
    people.sort()
    for i in range(N):
        num = people[i] // M * K	#손님 올 때까지 만들어진 붕어빵 갯수
        if num - i < 1:	#손님 올 때까지 만들어진 붕어빵 갯수-앞 사람들이 가져간 붕어빵 갯수 < 1 : impossible
            ans = "Impossible"
            break
    print("#{} {}".format(test_case, ans))