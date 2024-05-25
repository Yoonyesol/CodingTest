function solution(X, Y) {
    let arr = []
    let numA = new Array(10).fill(0);
    let numB = new Array(10).fill(0);
    
    for(let i=0; i < X.length; i++){
        numA[X[i]] += 1;
    }
    
    for(let i=0; i < Y.length; i++){
        numB[Y[i]] += 1;
    }
    
    for(let i=9; i >= 0; i--){
        if(numA[i] && numB[i]){
            let cnt = Math.min(numA[i], numB[i]);
            for(let j=0; j<cnt; j++){
                arr.push(i);
            }
        }
    }
    
    return arr.length ? (arr[0] === 0 ? 
                         "0" : arr.join("")): "-1";
}