function solution(array, commands) {
    var answer = [];
    for(let a of commands){
        let temp = []
        const [i, j, k] = a;
        temp = array.slice(i-1, j);
        temp.sort((a, b) => a - b);
        answer.push(temp[k-1]);
    }
    return answer;
}