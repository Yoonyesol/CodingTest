function solution(elements) {
    var answer = 0;
    let eSet = new Set();
    for(let i = 0; i < elements.length; i++){
        answer = elements[i];
        eSet.add(answer);
        for(let j = i+1; j < i+elements.length; j++){
            answer += elements[j%elements.length];
            eSet.add(answer)
        }
    }
    return eSet.size;
}