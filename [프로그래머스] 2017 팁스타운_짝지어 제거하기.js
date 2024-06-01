function solution(s)
{
    let stack = [];
    
    for(let i of s){
        if(!stack){
            stack.push(i);
        } else {
            if(stack[stack.length - 1] === i){
                stack.pop();
            } else {
                stack.push(i)
            }
        }
    }
    
    return stack.length ? 0 : 1;
}