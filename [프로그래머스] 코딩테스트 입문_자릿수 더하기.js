function solution(n) {
    n = n.toString()
    return n.split("").map((v) => Number(v)).reduce((acc, cur) => acc + cur);
}