function solution(keyinput, board) {
    let answer = [0, 0];
    let d = {"left":-1, "right":1, "up":1, "down":-1}
    for (let i of keyinput){
         if (i == "left" || i == "right"){
             answer[0] += d[i];
             if (Math.abs(answer[0]) > parseInt(board[0]/2)){
                 answer[0] -= d[i];
            }
         } else if (i == "up" || i == "down"){
             answer[1] += d[i];
             if (Math.abs(answer[1]) > parseInt(board[1]/2)){
                 answer[1] -= d[i];
            }
         }
    }
    return answer;
}