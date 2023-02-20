def solution(keyinput, board):
    answer = [0, 0]
    d = {"left":-1, "right":1, "up":1, "down":-1}
    for i in keyinput:
        if i in ["left", "right"]:
            answer[0] += d[i]
            if abs(answer[0]) > board[0]//2:
                answer[0] -= d[i]
        elif i in ["up", "down"]:
            answer[1] += d[i]
            if abs(answer[1]) > board[1]//2:
                answer[1] -= d[i]
    return answer