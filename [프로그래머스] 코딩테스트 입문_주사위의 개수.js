function solution(box, n) {
    var answer = 1;
    for (let i of box){
        answer *= parseInt(i / n)
    }
    return answer;
}

------------------------

function solution(box, n) {
    return box.reduce((acc, cur) => acc * parseInt(cur/n), 1);
}