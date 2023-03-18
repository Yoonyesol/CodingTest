function solution(balls, share) {
    function fac(n) { 
        let answer = BigInt(1);
        while(n > 0){
            answer *= BigInt(n);
            n--;
        }
        return BigInt(answer);
    }
    return fac(balls) / (fac(balls - share) * fac(share));
}
