function solution(a, b) {
    // 1. 기약분수 만들기
    let gcd = 1;
    for(let i = 2; i <= Math.min(a, b); i++){
        if(a % i === 0 && b % i === 0){
            gcd = i;
        }
    }
    b /= gcd;
    // 2. 분모에 2, 5 이외의 숫자가 곱해져 있는지 확인
    while(b % 2 == 0) { b /= 2 };
    while(b % 5 == 0) { b /= 5 };
    return b === 1 ? 1 : 2;
}