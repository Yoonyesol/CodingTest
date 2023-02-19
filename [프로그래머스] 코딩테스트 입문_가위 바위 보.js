function solution(rsp) {
    var dic = {"2":"0", "0":"5", "5":"2"}
    var answer = '';
    for(let i of rsp){
        answer += dic[i]
    }
    return answer;
}