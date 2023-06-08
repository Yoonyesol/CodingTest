from collections import deque
def solution(maps):
    answer = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    n, m = len(maps), len(maps[0])
    for i in range(n):
        maps[i] = list(maps[i])
    
    def bfs(x, y):
        global cnt
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            maps[x][y] = "X"
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= n or ny >= m or nx < 0 or ny < 0:
                    continue
                if maps[nx][ny] == "X":
                    continue
                cnt += int(maps[nx][ny])
                maps[nx][ny] = "X"
                queue.append((nx, ny))
    for i in range(n):
        for j in range(m):
            global cnt
            cnt = 0
            if maps[i][j] != "X":
                cnt += int(maps[i][j])
                bfs(i, j)
                answer.append(cnt)
    if answer:
        return sorted(answer)
    else:
        return [-1]