function solution(num, k) {
    if (num.toString().indexOf(k.toString()) == -1){
        return -1
    } else{
        return num.toString().indexOf(k.toString()) + 1;
    }
}