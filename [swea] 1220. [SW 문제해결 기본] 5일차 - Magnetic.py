T = 10
for test_case in range(1, T + 1):
    table = int(input())
    mgt = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    #열 순회
    for c in range(table):
        stack = []	#매 열마다 스택 초기화
        for r in range(table):
            if not stack and mgt[r][c] == 1:	#스택이 비어있고 N극(빨간색, 1)인 경우
                stack.append(1)	#1넣기
            elif stack and mgt[r][c] == 2:	#스택에 1이 들어있고 S극(파란색, 2)인 경우
                cnt += stack.pop()	#교착상태 짝이 맞으므로 1 pop
    print("#{} {}".format(test_case, cnt))


----------------------------------------


T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    arr = []
    ans = 0
    
    for _ in range(100):
        arr.append(list(map(int, input().split())))
        
    for i in range(100):
        n_flag = 0
        s_flag = 0
        for j in range(100):
            if arr[j][i] == 1:
                n_flag = 1
                s_flag = 0
            elif arr[j][i] == 2:
                s_flag = 1
                n_flag = 0
            if arr[j][i] == 0:
                if n_flag == 1:
                    arr[j][i] = 1
                elif s_flag == 1:
                    arr[j][i] = 2
                    
    for i in range(100):
        for j in range(99):
            if arr[j][i] == 1 and arr[j+1][i] == 2:
                ans += 1
                
    print("#{} {}".format(test_case, ans))