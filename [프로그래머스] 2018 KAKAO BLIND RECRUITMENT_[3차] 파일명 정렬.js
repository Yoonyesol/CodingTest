function solution(files) {
    let sortArr = [];
    for(let i = 0; i < files.length; i++){
        let answer = ['', '', '', i]
        for(let j = 0; j < files[i].length; j++){
            if(isNaN(parseInt(files[i][j])) === false){
                answer[0] = files[i].slice(0, j);
                answer[1] = files[i].slice(j);
                for(let k = 0; k < answer[1].length; k++){
                    if(answer[1][k] === " " || answer[1][k] === "." || answer[1][k] === "-"){
                        answer[2] = answer[1].slice(k);
                        answer[1] = answer[1].slice(0, k);
                        break;
                    }
                }
                sortArr.push(answer);
                break;
            }
        }
    }
    return sortArr.sort((a, b)=>{
        if(a[0].toLowerCase() > b[0].toLowerCase()){
            return 1;
        } else if(a[0].toLowerCase() < b[0].toLowerCase()){
            return -1;
        } else if(parseInt(a[1]) - parseInt(b[1]) !== 0){
            return parseInt(a[1]) - parseInt(b[1]);
        } else {
            return a[3] - b[3];
        }
    }).map((i) => [i[0], i[1], i[2]].join(''));
}
