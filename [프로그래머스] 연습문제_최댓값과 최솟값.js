function solution(s) {
    var answer = [];
    for(let i of s.split(" ")){
        answer.push(Number(i))
    }
    answer.sort((a, b)=>a-b)
    return `${answer[0]} ${answer[answer.length-1]}`;
}