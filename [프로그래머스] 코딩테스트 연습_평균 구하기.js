function solution(arr) {
    let answer = arr.reduce((acc, cur)=> acc + cur, 0);
    return answer/arr.length;
}