T = int(input())
for test_case in range(1, T + 1):
    mem = list(map(int, input()))
    check = 0
    if mem[0] == 1:	#첫번째 비트가 1인 경우 0->1로 바꿔주기
        check += 1
    for i in range(len(mem) - 1):
        if mem[i]  != mem[i+1]:	#앞 비트와 다른 비트가 나오는 경우 카운트+1
            check += 1
    print("#{} {}".format(test_case, check))


-----------------------------------

23.05.08
T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    flag = 0
    mem = list(map(int, input().rstrip()))
    for i in range(len(mem)):
        if (flag == 0 and mem[i] == 1) or (i >0 and mem[i] != mem[i-1]):
            answer += 1
            flag = 1
    print("#{} {}".format(test_case, answer))


--------------------------------------

25.05.17
T = int(input())
for test_case in range(1, T + 1):
    origin = list(input())
    b = "0" * len(list(origin))
    index = 0
    ans = 0

    while index < len(origin):
        if origin[index] != b[index]:
            ans += 1
            b = b[0:index] + origin[index] * len(b[index:])
        index += 1

    print('#{} {}'.format(test_case, ans))