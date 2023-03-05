function solution(record) {
    var answer = [];
    let userId = {};
    let status = {"Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."};
    for(let i of record){
        const arr = i.split(' ');
        if(arr[0] === "Enter" || arr[0] === "Change"){
            userId[arr[1]] = arr[2];
        }
    }
    for(let i of record){
        const arr = i.split(' ');
        if(arr[0] !== "Change"){
            answer.push(userId[arr[1]]+status[arr[0]]);
        }
    }
    return answer;
}