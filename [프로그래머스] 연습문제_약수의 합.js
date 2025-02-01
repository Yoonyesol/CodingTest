function solution(n) {
    let arr = new Set();
    for(let i = 1; i <= Math.sqrt(n); i++){
        if(n % i === 0){
            arr.add(i);
            arr.add(n / i);
        }
    }
    return [...arr].reduce((acc, num)=> acc + num, 0);
}

------------------

function solution(n) {
    let answer = 0
    let i;
    for(i = 1; i <= Math.sqrt(n); i++){
        if(n % i === 0){
            answer += (i + n/i)
        }
    }
    i--;
    return i === n/i ? answer - i : answer
}