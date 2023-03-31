function solution(name, yearning, photo) {
    var answer = [];
    let dic = {}
    for(let i = 0; i < name.length; i++){
        dic[name[i]] = yearning[i];
    }
    for(let i = 0; i < photo.length; i++){
        answer.push(0);
        for(let j of photo[i]){
            if(name.includes(j)){
                answer[i] += dic[j];
            }
        }
    }
    return answer;
}