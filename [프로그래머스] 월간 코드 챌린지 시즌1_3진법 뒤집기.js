function solution(n) {
    let a = n.toString(3).split("").join("")
    let answer = 0;
    for(let i = 0; i < a.length; i++){
        answer += Number(a[i]) * (3**i)
    }
    return answer;
}