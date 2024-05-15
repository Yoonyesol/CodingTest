function solution(n) {
    var answer = '';
    let arr = ["수", "박"]
    for(let i=0; i<n; i++){
        answer += arr[i%2]
    }
    return answer;
}