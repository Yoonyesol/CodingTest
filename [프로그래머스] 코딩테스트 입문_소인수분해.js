function solution(n) {
    var answer = [];
    let i = 2;
    while(i <= n){
        if(n % i == 0){
            n /= i
            if(!answer.includes(i)){
                answer.push(i);
            }            
        } else {
            i++;
        }
    }
    return answer;
}