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

--------------------------------

T = int(input())
for test_case in range(1, T+1):
    ans = "Possible"
    #n명, m초의 시간을 들여 k개의 붕어빵 제조
    n, m ,k = map(int, input().split())
    #각 초마다 사람이 도착
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(len(arr)):
        boong = arr[i]//m*k - i
        if boong <= 0:
            ans = "Impossible"
    print("#{} {}".format(test_case, ans))