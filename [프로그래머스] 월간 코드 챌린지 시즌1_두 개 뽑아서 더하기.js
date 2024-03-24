function solution(numbers) {
    var answer = [];
    numbers.forEach((it1, index1)=> {
         numbers.forEach((it2, index2)=>{
            if(index1!==index2){
                answer.push(it1+it2)
            }})
    })
    answer = [...new Set(answer)]
    return answer.sort((a, b)=>a-b);
}