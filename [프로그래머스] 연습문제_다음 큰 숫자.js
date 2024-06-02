function solution(n) {
    var answer = 0;
    let cnt = n.toString(2).split('').filter((it)=> it === '1').length;
    while (true){
        n++;
        let cnt2 = n.toString(2).split('').filter((it)=> it === '1').length;
        if(cnt2 === cnt){
            answer = n;
            break;
        }
    }
    return answer;
}