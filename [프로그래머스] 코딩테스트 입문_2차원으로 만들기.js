function solution(num_list, n) {
    var answer = [];
    for (let i = 0; i < parseInt(num_list.length/n); i++){
        answer.push([]);
    }
    for (let i = 0; i < num_list.length; i++){
        answer[parseInt(i/n)].push(num_list[i]);
    }
    return answer;
}