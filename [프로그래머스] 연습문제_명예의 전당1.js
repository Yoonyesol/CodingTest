function solution(k, score) {
    let arr = []
    var answer = [];
    score.forEach((it, idx)=>{
        if(arr.length >= k){
            arr.sort((a, b)=>a-b)
            if(it > arr[0]){
                arr.shift();
                arr.push(it);
            }
        } else {
            arr.push(it)
        }
        arr.sort((a, b)=>a-b)
        answer.push(arr[0])
    })
    return answer;
}