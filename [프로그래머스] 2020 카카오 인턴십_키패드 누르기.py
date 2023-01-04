def solution(numbers, hand):
    answer = ''
    key = {1:(0,0), 2:(0,1), 3:(0,2), 
           4:(1,0), 5:(1,1), 6:(1,2), 
           7:(2,0), 8:(2,1), 9:(2,2), 
           "*":(3,0), 0:(3,1), "#":(3,2)}
    l_hand, r_hand = key["*"], key["#"]
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            l_hand = key[i]
        if i in [3, 6, 9]:
            answer += "R"
            r_hand = key[i]
        if i in [2, 5, 8, 0]:
            left_hand = abs(l_hand[0]-key[i][0]) + abs(l_hand[1]-key[i][1])
            right_hand = abs(r_hand[0]-key[i][0]) + abs(r_hand[1]-key[i][1])
            if right_hand < left_hand:
                answer += "R"
                r_hand = key[i]
            elif right_hand > left_hand:
                answer += "L"
                l_hand = key[i]
            elif right_hand == left_hand:
                if hand == "right":
                    answer += "R"
                    r_hand = key[i]
                else:
                    answer += "L"
                    l_hand = key[i]
    return answer