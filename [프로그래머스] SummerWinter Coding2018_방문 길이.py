def solution(dirs):
    dic = {"U":(0, -1), "D":(0, 1), "R":(1, 0), "L":(-1, 0)}
    x, y = 0, 0
    xyset = set()
    
    for command in dirs:
        nx = x + dic[command][0]
        ny = y + dic[command][1]
        #벽면에 부딪친 경우 명령을 무시한다.
        if nx > 5 or ny > 5 or nx < -5 or ny < -5:
            continue
        xyset.add((y, x, ny, nx))   #start, end
        xyset.add((ny, nx, y, x))   #end, start
        x, y = nx, ny   #현재 위치를 이동한 좌표로 변경
    return len(xyset)//2