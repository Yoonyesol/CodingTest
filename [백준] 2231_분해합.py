import sys
N = int(sys.stdin.readline())
answer = 0
for i in range(N):
    num_list = list(map(int, str(i)))
    if (i + sum(num_list)) == N:
        answer = i
        break
print(answer)