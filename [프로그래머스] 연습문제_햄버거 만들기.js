function solution(ingredient) {
    var answer = 0;
    let arr = [];
    let str = ''
    for (let i of ingredient){
        arr.push(i)
        str = arr.slice(arr.length-4, arr.length).join('');
        if (arr.length >= 4 && str === '1231'){ //배열 그대로 비교할 수 없음(배열의 주소값을 비교함).따라서 문자열로 바꾸고 비교
            arr.splice(arr.length-4, 4); //.splice(-4)로 마지막 4개 삭제 가능
            answer++;
        }
    }
    return answer;
}