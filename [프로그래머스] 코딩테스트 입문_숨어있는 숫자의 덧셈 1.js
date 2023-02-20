function solution(my_string) {
    return my_string.split("").filter((el) => !isNaN(el)).map((v) => parseInt(v)).reduce((acc, cur)=> acc + cur);
}