function solution(num) {
    let answer = 0;
    if(num === 1) return 0;
    while(answer <= 500){
        if(answer === 500) return -1;
        num % 2 ? num = num * 3 + 1 : num /= 2
        answer++;
        if(num === 1) return answer;
    }
    return answer;
}