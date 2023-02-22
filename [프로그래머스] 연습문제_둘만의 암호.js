function solution(s, skip, index) {
    let answer = "";
    let alp = 'abcdefghijklmnopqrstuvwxyz';
    for(let i of skip){
        alp = alp.replace(i, "");
    }
    let arr = alp.split("");
    for(let j of s){
        answer += arr[(arr.indexOf(j) + index) % arr.length];
    }
    return answer;
}