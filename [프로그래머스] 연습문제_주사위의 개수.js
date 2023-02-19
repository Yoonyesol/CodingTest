function solution(box, n) {
    var answer = 1;
    for (let i of box){
        answer *= parseInt(i / n)
    }
    return answer;
}