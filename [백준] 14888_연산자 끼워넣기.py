import sys
input=sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

#최대 최소값 초기화
max_num = -1e9
min_num = 1e9

def dfs(idx, total, plus, minus, mul, div):
    global max_num, min_num
    #계산에 모든 수를 사용했다면, 최대값과 최소값을 출력
    if idx == n:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return
    if plus > 0:
        dfs(idx + 1, total + num[idx], plus-1, minus, mul, div)
    if minus > 0:
        dfs(idx + 1, total - num[idx], plus, minus-1, mul, div)
    if mul > 0:
        dfs(idx + 1, total * num[idx], plus, minus, mul-1, div)
    if div > 0:
        dfs(idx + 1, int(total / num[idx]), plus, minus, mul, div-1)
dfs(1, num[0], plus, minus, mul, div)
print(max_num)
print(min_num)



