const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = Number(input[0]);
// Please Write your code here.
function evenFive(a) {
    let answer = "No";
    const ten = parseInt(a / 10);
    const one = a % 10;

    if(a % 2 === 0 && (ten + one) % 5 === 0) {
        answer = "Yes";
    }

    return answer;
}

console.log(evenFive(n))