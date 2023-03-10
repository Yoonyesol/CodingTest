function solution(topping) {
    var answer = 0;
    let toppingDic = {}
    topping.forEach((i) => {
        i in toppingDic === false ? toppingDic[i] = 1 : toppingDic[i] += 1;
    })
    let toppingSet = new Set();
    let dicLen = Object.keys(toppingDic).length
    for(let i of topping){
        toppingDic[i] -= 1;
        toppingSet.add(i);
        if(toppingDic[i] === 0){
            dicLen -= 1;
        }
        if(dicLen === toppingSet.size){
            answer += 1;
        }
    }
    return answer;
}