function solution(str1, str2) {
    // 알파벳 체크 함수
    function isalpha(c){
        return (((c >= 'a') && (c <= 'z')) || ((c >= 'A') && (c <= 'Z')));
    }
    
    // 알파벳을 체크해 알파벳으로만 이루어진 쌍을 만들고 배열에 담아주는 함수
    function checkAlpha(string){
        let arr = []
        for(let i = 0; i < string.length - 1; i++){
            if(isalpha(string[i]) && isalpha(string[i+1])){
                arr.push(string[i].toUpperCase() + string[i+1].toUpperCase());
            }
        }
        return arr;
    }
   
    let arr1 = checkAlpha(str1);
    let arr2 = checkAlpha(str2);
    let setArr1 = [...new Set(arr1)];
    let setArr2 = [...new Set(arr2)];
    let kyo = 0;
    let hap = 0;
    
    for(let i of setArr1){
        if(arr2.includes(i) === true){
            kyo += Math.min(arr1.filter(el => el === i).length, arr2.filter(el => el === i).length);
            hap += Math.max(arr1.filter(el => el === i).length, arr2.filter(el => el === i).length);
        } else {
            hap += arr1.filter(el => el === i).length;
        }
    }
    for(let j of setArr2){
        if(arr1.includes(j) === false){
            hap += arr2.filter(el => el === j).length;
        }
    }    
    return hap === 0 ? 65536 : parseInt(kyo/hap * 65536);
}