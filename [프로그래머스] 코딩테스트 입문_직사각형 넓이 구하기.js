function solution(dots) {
    let dots2 = dots.sort()
    return (Math.abs(dots2[1][0]-dots2[3][0])) * (Math.abs(dots2[0][1]-dots2[1][1]));
}