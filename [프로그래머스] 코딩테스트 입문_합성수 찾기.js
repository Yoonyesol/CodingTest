function solution(n) {
    var answer = 0;
    for(let i = 4; i <= n; i++){
        let cnt = 1
        for(let j = 2; j <= n; j++){
            if(i % j === 0) { 
                cnt++;
            }
            if(cnt >= 3){
                answer++;
                break;
            } 
        }
    }
    return n <= 3 ? 0 :answer;
}

----------------------------------

function solution(n) {
    // i와 j 사이에 약수가 하나라도 존재하면 합성수
    var answer = 0;
    for(let i = 4; i <= n; i++){
        for(let j = 2; j < i; j++){
            if(i % j === 0) { 
                answer++;
                break;
            } 
        }
    }
    return answer;
}