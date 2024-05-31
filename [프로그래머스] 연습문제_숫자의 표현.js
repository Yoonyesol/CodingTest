function solution(n) {
    var answer = 0;
    var start = 1;
    var end = 1;
    var sum = 1;

    while (start <= n) {
        if (sum === n) {
            answer++;
            sum -= start;
            start++;
        } else if (sum < n) {
            end++;
            sum += end;
        } else {
            sum -= start;
            start++;
        }
    }

    return answer;
}
