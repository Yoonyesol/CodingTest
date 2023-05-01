from collections import deque                         
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def bfs(v):
        queue = deque()
        queue.append(v)
        while queue:
            x = queue.popleft()
            visited[x] = 1
            for i in range(n):
                if visited[i] == 0 and computers[x][i] == 1:
                    queue.append(i)
                    
    for i in range(n):
        if visited[i] == 0:
            bfs(i)
            answer += 1
    return answer