const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(" ");
let n = Number(input[0]);
let m = Number(input[1]);
// Please Write your code here.

function GCD(a, b){
    //a, b 중 더 큰 숫자 찾기
    if(b > a) {
        [a, b] = [b, a];
    }

    while(b !== 0) {
        let temp = b;
        b = a % b; //a를 b로 나눈 나머지를 b에 저장
        a = temp; //원래의 b값을 a에 저장
    } 

    return a; //b === 0일 때, a값이 최대공약수
}

console.log(GCD(n, m));