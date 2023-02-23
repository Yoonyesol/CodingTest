function solution(my_string, n) {
    var answer = '';
    my_string.split("").forEach((item)=> answer += item.repeat(n))
    return answer;
}