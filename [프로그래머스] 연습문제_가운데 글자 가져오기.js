function solution(s) {
    var answer = '';
    return s.length % 2 === 1? 
        s[Math.floor(s.length/2)] 
        : s.slice((s.length/2)-1,(s.length/2)+1);
}