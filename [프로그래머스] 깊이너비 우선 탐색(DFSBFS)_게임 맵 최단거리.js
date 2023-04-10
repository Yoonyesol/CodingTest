function solution(maps) {   
    n = maps.length
    m = maps[0].length
    
    let dx = [-1, 1, 0, 0]
    let dy = [0, 0, -1, 1]
    
    function bfs(x, y){
        queue = [[x, y]]
        maps[x][y] = 1
        while (queue.length > 0){
            [x, y] = queue.shift()
            for(let i = 0; i < 4; i++){
                let nx = x + dx[i]
                let ny = y + dy[i]
                if (nx >= n || ny >= m || nx < 0 || ny < 0){
                    continue;
                }
                if (maps[nx][ny] === 0){
                    continue
                }
                if (maps[nx][ny] === 1){
                    maps[nx][ny] = maps[x][y] + 1
                    queue.push([nx, ny])
                }
                if (nx === n-1 && ny === m-1){
                    return maps[nx][ny]
                }
            }
        }
        return -1
    }
    return bfs(0,0);
}