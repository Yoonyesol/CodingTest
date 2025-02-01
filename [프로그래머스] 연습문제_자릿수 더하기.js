function solution(n)
{
    return (''+n).split('').reduce((acc, num) => acc + Number(num) , 0);
}