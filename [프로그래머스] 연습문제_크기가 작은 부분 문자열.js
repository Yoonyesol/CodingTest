function solution(t, p) {
    var answer = 0;
    let pl = p.length;
    let str = ''
    
    for(let i=0; i <= t.length-pl; i++){
        str = t.slice(i, i+pl);
        if (parseInt(str) <= parseInt(p)){
            answer++;
        }
    }
    return answer;
}