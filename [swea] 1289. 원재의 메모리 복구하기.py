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