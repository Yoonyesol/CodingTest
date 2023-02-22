function solution(sides) {
    var answer = 0;
    for(let i = Math.max(...sides) - Math.min(...sides) + 1; i <= Math.max(...sides); i++){
        answer++;
    }
    for(let i = Math.max(...sides) + 1; i < sides[0] + sides[1]; i++){
        answer++;
    }
    return answer;
}