function solution(strings, n) {
    strings.sort((prev, cur)=>{
        return prev[n] === cur[n] ? 
            prev.localeCompare(cur): prev[n].localeCompare(cur[n]);
    })
    return strings;
}