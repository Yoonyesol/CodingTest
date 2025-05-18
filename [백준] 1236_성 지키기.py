n, m = map(int, input().split())
arr = []
cnt1, cnt2 = 0, 0
for _ in range(n):
    arr.append(list(input()))
for i in range(n):
    if 'X' not in arr[i]:
        cnt1 += 1

for j in range(m):
    for i in range(n):
        if arr[i][j] == 'X':
            break
    else:
        cnt2 += 1
print(max(cnt1, cnt2))