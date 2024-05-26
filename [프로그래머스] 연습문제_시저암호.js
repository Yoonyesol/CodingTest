function solution(s, n) {
    var answer = '';
    let num;
    for(let i of s){
        if(i === " "){
            answer += " ";
            continue
        } 
        
        let j = i.charCodeAt()
        if(j >= 97){ //소문자
            num = (j - 97 + n) % 26 + 97;
        } else {
            num = (j -65 + n) % 26 + 65;
        }
        answer += String.fromCharCode(num);
    }
    return answer;
}