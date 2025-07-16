const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

let [a, b, c] = input[0].split(" ").map(Number);

// Please Write your code here.
function minNum(a, b, c){
    return Math.min(a, b, c)
}

console.log(minNum(a, b, c))