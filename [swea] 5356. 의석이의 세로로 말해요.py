T = int(input())
for test_case in range(1, T + 1):
    arr = []
    for _ in range(5):
        a = input()
        a += "*" * (15 - len(a))
        arr.append(a)
    answer = ['' for _ in range(15)]
    for i in range(15):
        for j in range(5):
            answer[i] += arr[j][i]
    print("#{}".format(test_case), end=" ")
    for i in range(15):
        answer[i] = answer[i].replace("*", "")
        print(answer[i], end="")
    print()