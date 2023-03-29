function solution(skill, skill_trees) {
    var answer = 0;
    for(let i of skill_trees){
        let arr = skill.split('');
        let flag = 1;
        for(let j of i){
            if(arr.includes(j)){
                if(j !== arr.shift()){
                    flag = 0;
                    break;
                }
            }
            
        }
        if(flag === 1)  {answer++;}
    }
    return answer;
}