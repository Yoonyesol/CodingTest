function solution(sides) {
    return Math.max(...sides) < sides.reduce((acc, cur)=> acc+cur) - Math.max(...sides) ? 1: 2;
}