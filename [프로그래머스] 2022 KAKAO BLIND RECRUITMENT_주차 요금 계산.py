import math
def solution(fees, records):
    answer = []
    temp = {}
    parking = {}
    
    for record in records:
        time, car, inout = record.split()
        if car not in temp:
            temp[car] = time
        else:
            if inout == "OUT":
                parkingTime = (int(time.split(":")[0]) * 60 + int(time.split(":")[1])) - (int(temp[car].split(":")[0]) * 60 + int(temp[car].split(":")[1]))
                if car not in parking:
                    parking[car] = parkingTime
                else:
                    parking[car] += parkingTime
                del(temp[car])
                
    for remain in temp.keys():
        parkingTime = 23 * 60 + 59 - (int(temp[remain].split(":")[0]) * 60 + int(temp[remain].split(":")[1]))
        if remain not in parking:
            parking[remain] = parkingTime
        else:
            parking[remain] += parkingTime
            
    for i in parking.keys():
        totalPay = fees[1] + math.ceil(max(0, (parking[i] - fees[0])) / fees[2]) * fees[3]
        parking[i] = totalPay
        
    for i in sorted(parking.items()):
        answer.append(i[1])
        
    return answer