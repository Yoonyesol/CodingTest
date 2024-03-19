function solution(a, b, n) {
    var answer = 0;
    let c = 0;
    while(n >= a){
        c = parseInt(n / a);
        n = n - (c * a) + (c * b);
        answer += (c * b);
    }
    return answer;
}

------------------------------------

function solution(a, b, n) {
    var answer = 0;
    while(n >= a){
         answer += b;
        n = n - a + b;
    }
    return answer;
}