function solution(N, stages) {
    var answer = [];
    for(let i = 1; i <= N; i++){
        //시도한 사람
        const tried = stages.filter((it)=> it >= i).length;
        //실패한 사람
        const failed = stages.filter((it)=> it === i).length;
        
        answer.push([i, (failed/tried)]);
    }  
    
    answer.sort((a, b) => b[1] - a[1])
    return answer.map((it) => it[0]);
}