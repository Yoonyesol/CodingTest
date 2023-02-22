def solution(board):
    newlist = [[i,j] for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 1]
    answer = len(newlist)
    for n in newlist:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if 0 <= n[0]+i < len(board) and 0 <= n[1]+j < len(board):
                    if board[n[0]+i][n[1]+j] == 0:
                        board[n[0]+i][n[1]+j] = 1
                        answer += 1
    return len(board)**2 - answer

-----------------------------------

def solution(board):
    newlist = [[i,j] for i in range(len(board)) for j in range(len(board[i])) if board[i][j]==1]
    answer = len(newlist)
    x_arr = [-1, -1, -1, 0, 0, 1, 1, 1]
    y_arr = [-1, 0, 1, -1, 1, -1, 0, 1]
    for x, y in newlist:
        for i in range(8):
            new_x = x + x_arr[i]
            new_y = y + y_arr[i]
            if 0 <= new_x < len(board) and 0 <= new_y < len(board):
                if board[new_x][new_y] == 0:
                    board[new_x][new_y] = 1
                    answer += 1
    return len(board)**2 - answer