T = int(input())
for test_case in range(1, T + 1):
    h, w = map(int, input().split())
    board = []
    for _ in range(h):
        board.append(list(input()))
    input()
    str_arr = input()
    px, py = 0, 0
    head = ""
    for i in range(h):
        for j in range(w):
            if board[i][j] in ["^", "v", "<", ">"]:
                px = j
                py = i
                head = board[i][j]
                board[i][j] = "."
                break
    dic = {"U":"^", "D":"v", "L":"<", "R":">"}
    for k in str_arr:
        if k == "U":
            head = dic[k]
            if py-1 >= h or px >= w or py-1 < 0 or px < 0:
                continue
            if board[py-1][px] == ".":
                board[py][px] = "."
                py -= 1
        elif k == "D":
            head = dic[k]
            if py+1 >= h or px >= w or py+1 < 0 or px < 0:
                continue
            if board[py+1][px] == ".":
                board[py][px] = "."
                py += 1
        elif k == "L":
            head = dic[k]
            if py >= h or px-1 >= w or py < 0 or px-1 < 0:
                continue
            if board[py][px-1] == ".":
                board[py][px] = "."
                px -= 1
        elif k == "R":
            head = dic[k]
            if py >= h or px+1 >= w or py < 0 or px+1 < 0:
                continue
            if board[py][px+1] == ".":
                board[py][px] = "."
                px += 1
        elif k == "S":
            if head == "^":
                for a in range(py, -1, -1):
                    if board[a][px] == "#":
                        break
                    if board[a][px] == "*":
                        board[a][px] = "."
                        break
            elif head == "v":
                for a in range(py, h):
                    if board[a][px] == "#":
                        break
                    if board[a][px] == "*":
                        board[a][px] = "."
                        break
            elif head == "<":
                for b in range(px, -1, -1):
                    if board[py][b] == "#":
                        break
                    if board[py][b] == "*":
                        board[py][b] = "."
                        break
            elif head == ">":
                for b in range(px, w):
                    if board[py][b] == "#":
                        break
                    if board[py][b] == "*":
                        board[py][b] = "."
                        break
    board[py][px] = head
    print("#{}".format(test_case), end=" ")
    for i in range(h):
        for j in range(w):
            print(board[i][j], end="")
        print()