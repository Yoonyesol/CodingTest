function solution(numbers) {
    let sum = 9 * (9 + 1) / 2
    var answer = numbers.reduce((acc, cur)=> acc + cur, 0);
    return sum-answer;
}