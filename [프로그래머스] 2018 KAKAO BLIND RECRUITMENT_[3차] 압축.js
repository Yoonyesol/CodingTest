function solution(msg) {
    var answer = [];
    let dic = {};
    for(let i = 1; i <= 26; i++){
        dic[String.fromCodePoint(64+i)] = i
    }
    let checkMsg = "";
    let idx = 27;
    for(let i of msg){
        checkMsg += i;
        if(Object.keys(dic).includes(checkMsg) === false){
            answer.push(dic[checkMsg.slice(0, checkMsg.length -1)]);
            dic[checkMsg] = idx
            idx += 1
            checkMsg = checkMsg[checkMsg.length-1];
        }
    }
    answer.push(dic[checkMsg]);
    return answer;
}