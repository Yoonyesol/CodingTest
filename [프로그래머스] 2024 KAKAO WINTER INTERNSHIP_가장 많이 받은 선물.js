function solution(friends, gifts) {
    let dic = {};
    //친구별 준 선물리스트, 받은 선물리스트, 다음 달에 받을 선물갯수 초기화
    for(let friend of friends){
        dic[friend] = [[], [], 0]
    }
    
    //친구별 준 선물, 받은 선물 리스트 저장
    for (let i of gifts){
        let [a, b] = i.split(' ')
        dic[a][0].push(b)   //a가 b에게 준 선물
        dic[b][1].push(a)   //b가 a에게 받은 선물
    }
    
    let answer = 0  //최대값 체크 변수
    let dup_check = new Set();  //중복 체크 set
    for(let i of friends){
        for(let j of friends){
            if(i === j) continue
            if(dup_check.has(i+j)) continue //이미 체크한 친구들 쌍이라면 pass
            
            //i가 j에게 준 선물 갯수
            let c = dic[i][0].filter((it)=>it===j).length;
            //j가 i에게 준 선물 갯수
            let d = dic[j][0].filter((it)=>it===i).length;
                
            //i가 j에게 더 선물을 많이 준 경우
            if(c > d){  
                dic[i][2] += 1  //i의 선물갯수++
            } else if(c === d){
                //선물지수 계산
                let iGiftNum = dic[i][0].length - dic[i][1].length;
                let jGiftNum = dic[j][0].length - dic[j][1].length;
                    
                //j의 선물지수가 더 큰 경우
                if(iGiftNum < jGiftNum){
                    dic[j][2] += 1  //j가 다음달에 선물을 받음
                } else if(iGiftNum > jGiftNum)  {
                    dic[i][2] += 1
                }
            } else {
                dic[j][2] += 1
            }
            dup_check.add(i+j)
            dup_check.add(j+i)
        }
        answer = Math.max(dic[i][2], answer) //매번 친구 리스트를 돌면서 다음 달에 선물 받을 갯수의 max를 구하기
    }
    return answer;
}