function solution(s) {
    var answer = [0, 0];
    while(s !== "1"){
        let sArr = s.split("")
        let len = sArr.filter((it)=> it === '1').length;
        answer[1] += sArr.length - len;
        s = len.toString(2);
        answer[0]++;
    }
    return answer;
}