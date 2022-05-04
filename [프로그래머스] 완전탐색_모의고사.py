def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0,0,0]
    max_score = 0
    for i in range(len(answers)):
        if(s1[i%5] == answers[i]): scores[0] = scores[0] + 1
        if(s2[i%8] == answers[i]): scores[1] = scores[1] + 1
        if(s3[i%10] == answers[i]): scores[2] = scores[2] + 1
    max_score = max(scores)
    for i in range(len(scores)):
        if (scores[i] == max_score):
            answer.append(i+1)
    return answer