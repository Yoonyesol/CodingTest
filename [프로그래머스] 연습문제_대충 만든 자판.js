function solution(keymap, targets) {
    var answer = Array(targets.length).fill(0);
    let dic = {};
    for(let i of keymap){
        for(let j of i){
            if(j in dic){
                dic[j] = Math.min(dic[j], i.indexOf(j) + 1);
            } else {
                dic[j] = i.indexOf(j) + 1;
            }
        }
    }
    for(let i = 0; i < targets.length; i++){
        for(let j of targets[i]){
            if(j in dic){
                answer[i] += dic[j]
            } else {
                answer[i] = -1; 
                break;
            }
        }
    }
    return answer;
}