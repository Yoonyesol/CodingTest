function solution(s) {
    var answer = 0;
    while(s.length > 1){
        x_cnt = 0;
        cnt = 0;
        let x = s[0]
        for(let i of s){
            if(i === x){
                x_cnt++;
            }else {
                cnt++;
            }
            if(x_cnt === cnt){
                s = s.slice(x_cnt + cnt);
                answer++;
                break;
            }
        }
        if(x_cnt !== cnt) break;
    }
    if (s.length > 0){
        answer++;
    }
    return answer;
}