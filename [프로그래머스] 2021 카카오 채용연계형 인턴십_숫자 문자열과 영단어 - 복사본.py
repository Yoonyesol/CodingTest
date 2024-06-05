function solution(s) {
    var answer = 0;
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for(let i=0; i<10; i++){
        s = s.replaceAll(arr[i], i)
    }
    return Number(s);
}