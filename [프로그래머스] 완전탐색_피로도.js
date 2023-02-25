let answer = 0
let cnt = 0
let visited;

function DFS(k, cnt, dungeons){
    if(cnt > answer){
        answer = cnt;
    }
    for(let i = 0; i < dungeons.length; i++){
        if(k >= dungeons[i][0] && visited[i] == 0){
            visited[i] = 1;
            DFS(k - dungeons[i][1], cnt+1, dungeons);
            visited[i] = 0;
        }
    }
}

function solution(k, dungeons) {
    (visited = []).length = dungeons.length;
    visited.fill(0);
    DFS(k, 0, dungeons);
    return answer;
}