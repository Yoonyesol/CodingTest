function solution(n, m, section) {
    var answer = 0;
    while(section.length > 0){
        e = section[0];
        while(section.length > 0 && e <= section[0] && section[0] < e+m){
            section.shift();    
        }
        answer++;
    }
    return answer;
}