const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = Number(input[0]);
// Please write your code here.
function sqaure (N) {
    cnt = 0;
    for(let i = 0; i < N; i++){
        arr = [];
        j = 0;
        while (j < N) {
            arr.push(cnt % 9 + 1);
            j++;
            cnt++;
        }
        console.log(arr.join(' '))
    }
}

sqaure(N);
