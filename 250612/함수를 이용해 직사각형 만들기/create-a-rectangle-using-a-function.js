const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");
let [n, m] = input[0].split(" ").map(Number);

// Please Write your code here.
function square (n, m) {
    for(let i = 0; i < n; i++) {
        const a = '1'.repeat(m)
        console.log(a)
    }
}

square(n, m);