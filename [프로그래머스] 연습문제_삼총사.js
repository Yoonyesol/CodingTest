function solution(number) {
    var answer = 0;
    for (let i = 0; i < number.length; i++){
        for (let j = 0; j < number.length; j++){
            if (i === j) break;
            for (let k = 0; k < number.length; k++){
                if (i === k || j === k) break;
                if (number[i]+number[j]+number[k] === 0){
                    console.log(i, j, k)
                    answer++
                }
            }
        }
    }
    return answer;
}