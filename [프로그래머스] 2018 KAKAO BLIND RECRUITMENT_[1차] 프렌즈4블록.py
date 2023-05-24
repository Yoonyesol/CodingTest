def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    total = 0
    
    while True:
        aset = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '':
                    continue
                if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i+1][j] == board[i+1][j+1]:
                    aset.add((i, j))
                    aset.add((i+1, j))
                    aset.add((i, j+1))
                    aset.add((i+1, j+1))
        
        if len(aset) == 0: break
        
        #aset에 저장된 좌표들을 모두 공백으로 바꾸기
        for i, j in aset:
            board[i][j] = ''
        
        #블록 떨어뜨리기
        while True:
            flag = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == '':
                        board[i+1][j] = board[i][j]
                        board[i][j] = ''
                        flag = 1
            if flag == 0: break
        total += len(aset)
    return total