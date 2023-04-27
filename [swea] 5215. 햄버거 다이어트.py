def dfs(v, t_sum, k_sum):
    global max_taste
    if k_sum > l:	#칼로리 합이 l을 넘어서면 종료
        return
    if max_taste < t_sum:	#max_taste 값 갱신
        max_taste = t_sum
    if v == n:	#마지막 노드까지 탐색한 경우 종료
        return
    taste, kcal = arr[v]	#현재 인덱스의 노드에서 taste, kcal 꺼냄
    
    #재료를 사용한 경우(현재 인덱스 노드의 taste, kcal 더하기)
    dfs(v+1, t_sum+taste, k_sum+kcal)
    #재료를 사용하지 않은 경우
    dfs(v+1, t_sum, k_sum)

T = int(input())
for test_case in range(1, T + 1):
    n, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_taste = 0
    dfs(0, 0, 0)
    print("#{} {}".format(test_case, max_taste))