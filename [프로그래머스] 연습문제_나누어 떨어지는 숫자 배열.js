function solution(arr, divisor) {
    var answer = [];
    answer = arr.filter(item => item % divisor === 0).sort((a, b) => a-b)
    return answer.length === 0 ? [-1]: answer;
}