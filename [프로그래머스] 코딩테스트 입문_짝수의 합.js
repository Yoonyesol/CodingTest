function solution(n) {
    var answer = 0;
    for(let i = 0; i <= n; i++) { (i % 2 === 0) ? answer += i : answer += 0}
    return answer;
}