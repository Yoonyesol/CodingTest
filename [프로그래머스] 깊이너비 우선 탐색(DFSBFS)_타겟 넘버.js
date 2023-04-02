function solution(numbers, target) {
    var answer = 0;
    function DFS(idx, result){
        if(idx === numbers.length){
            if(result === target){
                answer += 1
            }
            return
        }
        DFS(idx+1, result - numbers[idx])
        DFS(idx+1, result + numbers[idx])
    }
    DFS(0,0);
    return answer;
}