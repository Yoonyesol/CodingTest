const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

let [n, m] = input[0].split(' ').map(Number);

function GCD (a, b) {
    if(a < b) {
        [b, a] = [a, b];
    }

    while(b !== 0){
        let temp = b;
        b = a % b;
        a = temp;
    }

    return a;
}

// Please Write your code here.
function LCM (a, b) {
    const gcd = GCD(a, b);
    return (a * b) / gcd
}

console.log(LCM(n, m))