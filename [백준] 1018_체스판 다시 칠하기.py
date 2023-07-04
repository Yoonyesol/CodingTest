import sys
input=sys.stdin.readline
n, m = map(int, input().split())
chess = [[] for _ in range(n)]
for i in range(n):
    chess[i] = input().rstrip()
ans_arr = []
for i in range(n-7):
    for j in range(m-7):
        ans1 = 0    #시작 지점이 Black
        ans2 = 0    #시작 지점이 White
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k+l)%2 == 0:    #행+열이 짝수인 경우, 시작점 색깔과 현재 판의 색이 동일해야 한다
                    if chess[k][l] != 'B':  #해당 판의 색이 Black이 아닌 경우,
                        ans1 += 1   #시작점이 B라면 색칠하기
                    if chess[k][l] != 'W':
                        ans2 += 1
                else:   #행+열이 홀수인 경우, 시작점 색깔과 현재 판의 색이 달라야 한다
                    if chess[k][l] != 'W':
                        ans1 += 1
                    if chess[k][l] != 'B':
                        ans2 += 1
        ans_arr.append(ans1)
        ans_arr.append(ans2)
print(min(ans_arr))