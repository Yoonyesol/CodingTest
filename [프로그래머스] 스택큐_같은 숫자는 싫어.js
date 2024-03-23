function solution(arr)
{    
    var answer = [];
    arr.forEach((num)=>{
        if(answer[answer.length-1] !== num) {
            answer.push(num)
        }
    })
    
    return answer;
}