function solution(arr) {
    const min = arr.reduce((a, b) => Math.min(a, b), Infinity);
    arr.forEach((item, index)=>{
        if (item === min){
            arr.splice(index, 1);
        }
    })
    return arr.length === 0 ? [-1]: arr;
}