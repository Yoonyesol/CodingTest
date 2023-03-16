function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let ing = Array(bridge_length).fill(0);
    let check = 0;
    while(ing.length > 0){
        answer++;
        check -= ing.shift();
        if(truck_weights.length > 0){
            if(check + truck_weights[0] <= weight){
                ing.push(truck_weights.shift());
                check += ing[ing.length - 1];
            } else {
                ing.push(0);
            }
        }
    }
    return answer;
}