T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [0] * n
    answer = 0

    def dfs(x):
        global answer
        if x == n:  #n행의 depth까지 들어갔다면
            answer += 1     #퀸 놓는 경우의 수+1
            return
        for i in range(n):  #n행 반복
            board[x] = i    #x행, i열에 퀸 놓기
            for j in range(x):
                #동일한 열에 있거나 or 대각선상에 있을 때 퀸 놓기 불가
                if board[x] == board[j] or abs(board[x]-board[j]) == abs(x-j):
                    break
            #break문 실행이 되지 않았을 때 -> 퀸을 놓을 수 있다.
            else:
                dfs(x+1)    #다음 재귀 실행해서 새로운 퀸 놓기
    dfs(0)
    print("#{} {}".format(test_case, answer))