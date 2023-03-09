function solution(numbers) {
    let dic = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"};
    for(let i = 0; i <= 9; i++){
        if(numbers.includes(dic[i])){
            numbers = numbers.replaceAll(dic[i], i);
        }
    }
    return Number(numbers);
}