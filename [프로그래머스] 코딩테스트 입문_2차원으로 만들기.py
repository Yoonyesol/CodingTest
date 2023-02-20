def solution(num_list, n):
    answer = [[] for _ in range(len(num_list)//n)]
    for i in range(len(num_list)):
        answer[i//n].append(num_list[i])
    return answer