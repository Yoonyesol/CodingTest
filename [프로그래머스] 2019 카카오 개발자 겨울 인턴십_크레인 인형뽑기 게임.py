def solution(board, moves):
    answer = 0
    stack = []
    for k in moves:
        for i in range(len(board)):
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
            for j in range(len(board[0])):
                if k-1 == i:
                    if board[j][i] != 0:
                        stack.append(board[j][i])
                        board[j][i] = 0
                        break                    
    return answer