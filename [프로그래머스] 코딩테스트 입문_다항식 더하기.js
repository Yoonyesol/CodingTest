function solution(polynomial) {
    let arr = polynomial.split(" + ")
    let x = 0
    let num = 0
    for(let i of arr){
        if(i.includes("x")){
            i === "x" ? x += 1 : x += parseInt(i);
        } else {
            num += parseInt(i);
        }
    }
    if(x > 0 && num > 0){
        return x === 1 ? "x + " + num.toString() : x.toString() + "x + " + num.toString();
    } else if(x == 0){
        return num.toString();
    } else if(num == 0){
        return x === 1 ? "x" : x.toString() + "x";
    }
}