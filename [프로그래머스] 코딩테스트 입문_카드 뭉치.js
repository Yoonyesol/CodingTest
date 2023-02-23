function solution(cards1, cards2, goal) {
    for(let i of goal){
        if (cards1 && cards1[0] == i){
            cards1.shift()
        } else if(cards2 && cards2[0] == i){
            cards2.shift()
        } else {
            return "No";
        }
    }
    return "Yes";
}