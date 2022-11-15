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