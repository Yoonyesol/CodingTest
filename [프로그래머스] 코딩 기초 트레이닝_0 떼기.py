def solution(n_str):
    idx = 0
    for i in range(len(n_str)):
        if n_str[i] != "0":
            idx = i
            return n_str[i:]