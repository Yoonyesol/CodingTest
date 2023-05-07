def dfs(cnt):
    global answer
    if cnt == t:
        temp = ''.join(num)
        answer = max(answer, temp)
        return
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]
            temp = ''.join(num)
            if visited.get((temp, cnt), 1):
                visited[(temp, cnt)] = 0
                dfs(cnt+1)
            num[i], num[j] = num[j], num[i]
T = int(input())
for test_case in range(1, T + 1):
    num, t = input().split()
    num = list(num)
    t = int(t)
    answer = "00000000"
    visited = {}
    dfs(0)
    print(visited)
    print("#{} {}".format(test_case, answer))