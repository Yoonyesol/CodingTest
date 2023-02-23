function solution(want, number, discount) {
    var answer = 0;
    let dic = {};
    for(let i = 0; i < want.length; i++){
        dic[want[i]] = number[i];
    }
    for(let i = 0; i <= discount.length - 10; i++){
        let check = 0;
        for(let key in dic){
            if(dic[key] > discount.slice(i, i+10).filter((el)=> el === key).length){
                check = 0;
                break;
            }
            check = 1;
        }
        answer += check;
    }
    return answer;
}