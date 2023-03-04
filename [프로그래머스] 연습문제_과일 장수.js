function solution(k, m, score) {
    var answer = 0;
    apple = score.sort((a, b) => b - a)
    let i = 0
    while(true){
        if(apple.slice(i, i + m).length < m){
            return answer;
        }
        answer += apple.slice(i, i + m).at(-1) * m
        i += m
    }
}