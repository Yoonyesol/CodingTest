const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = Number(input[0]);
// Please Write your code here.

function hap (n){
    let result = 0;
    for(let i = 1; i <= n; i++){
        result += i;
    }
    return parseInt(result / 10);
}

console.log(hap(n))