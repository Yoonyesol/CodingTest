function solution(s) {
    var answer = s[0].toUpperCase();
    let sArr = s.split("")
    for(let i = 1; i < sArr.length; i++){
        if(isNaN(sArr[i])){
            if(sArr[i-1] === " "){
                sArr[i] = sArr[i].toUpperCase()
            } else {
                sArr[i] = sArr[i].toLowerCase()
            }
        }
        answer += sArr[i]
    }
    return answer;
}