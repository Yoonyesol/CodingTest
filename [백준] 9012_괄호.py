import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    ans = "NO"
    ps = list(input().rstrip())
    stack = []
    for i in ps:
        if i == "(":
            stack.append(i)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                break
    else:
        if not stack:
            ans = "YES"
    print(ans)