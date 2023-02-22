function solution(board) {
    let arr = [];
    for (let i = 0; i < board[0].length; i++){
        for (let j = 0; j < board[0].length; j++){
            if (board[i][j] === 1){
                arr.push([i,j]);
            }
        }
    }
    let answer = arr.length;
    for (let k of arr){
        for (let l of [-1, 0, 1]){
            for (let m of [-1, 0, 1]){
                if ((0 <= (k[0]+l) && (k[0]+l) < board[0].length) && (0 <= (k[1]+m) && (k[1]+m) < board[0].length)){
                    if (board[k[0]+l][k[1]+m] === 0){
                        board[k[0]+l][k[1]+m] = 1
                        answer++;
                    }
                }
            }
        }
    }
    return board.length ** 2 - answer;
}