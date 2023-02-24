function solution(numbers, direction) {
    if (direction === "right"){
        numbers.splice(0, 0, numbers.pop());
    } else {
        numbers.push(numbers.shift());
    } 
    return numbers;
}