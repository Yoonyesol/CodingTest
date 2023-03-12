function solution(lines) {
    let answer = Array(200).fill(0);
    let cnt = 0;
    for(let i of lines){
        for(let j = i[0]; j < i[1]; j++){
            answer[j + 100]++;
            if(answer[j + 100] === 2){ cnt++; }
        }
    }
    return cnt;
}