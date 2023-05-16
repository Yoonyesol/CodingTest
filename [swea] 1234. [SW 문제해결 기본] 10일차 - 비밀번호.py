T = 10
for test_case in range(1, T+1):
    n, m = input().split()
    stack = []
    for i in range(int(n)):
        if not stack:
            stack.append(m[i])
        else:
            if stack[-1] == m[i]:
                stack.pop()
            else:
                stack.append(m[i])
    print("#{} {}".format(test_case, ''.join(stack)))