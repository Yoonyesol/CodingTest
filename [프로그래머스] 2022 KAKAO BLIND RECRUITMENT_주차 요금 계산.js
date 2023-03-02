function solution(fees, records) {
    var answer = [];
    let temp = {};
    var parking = {};
    let parkingTime = 0;
    
    for(let i of records){
        let [time, car, inout] = i.split(' ');
        if(car in temp == false){
            temp[car] = time;
        } else{
            if(inout === "OUT"){
                parkingTime = (Number(time.split(':')[0]) * 60 + Number(time.split(':')[1])) - (Number(temp[car].split(':')[0]) * 60 + Number(temp[car].split(':')[1]));
                if(car in parking === false){
                    parking[car] = parkingTime;
                } else{
                    parking[car] += parkingTime;
                }
                delete temp[car];
            }
        }
    }

    for(let i in temp){
        if(i in parking === false){
            parking[i] = 23 * 60 + 59 - (Number(temp[i].split(':')[0]) * 60 + Number(temp[i].split(':')[1]));
        } else{
            parking[i] += 23 * 60 + 59 - (Number(temp[i].split(':')[0]) * 60 + Number(temp[i].split(':')[1]));
        }
    }

    for(let i in parking){
        let parkingPay = fees[1] + Math.ceil((Math.max(0, parking[i] - fees[0])) / fees[2]) * fees[3];
        answer.push([i, parkingPay]);
    }
    return answer.sort((a, b) => a[0] - b[0]).map(v => v[1]);
}