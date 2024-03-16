function solution(s) {
    let cnt = 0;
    var answer = [];
    for(let i of s){
        let strIndex = s.substr(0, cnt).lastIndexOf(i);
        if (strIndex === -1){
            answer.push(-1)
        } else {
            answer.push(cnt - strIndex)
        }
        cnt++;
    }
    return answer;
}