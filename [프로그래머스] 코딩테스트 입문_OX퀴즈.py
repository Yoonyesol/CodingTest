def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        quiz[i] = quiz[i].split(" ")
        if quiz[i][1] == "+":
            if int(quiz[i][0]) + int(quiz[i][2]) == int(quiz[i][4]):
                answer.append("O")
            else:
                answer.append("X")
        elif quiz[i][1] == "-":
            if int(quiz[i][0]) - int(quiz[i][2]) == int(quiz[i][4]):
                answer.append("O")
            else:
                answer.append("X") 
    return answer