const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const [A, B] = input[0].split(" ").map(Number);

function threeSixNineIncludes (a) {
    const str = String(a);
    let answer = false;

    if(str.includes('3') || str.includes('6') || str.includes('9')){
        answer = true;
    }

    return answer;
}

// Please Write your code here.
function threeSixNine (a, b) {
    let cnt = 0;
    for (let i = a; i <= b; i++) {
        if(threeSixNineIncludes(i) || i % 3 === 0) {
            cnt++;
        }
    }
    return cnt;
}

console.log(threeSixNine(A, B))