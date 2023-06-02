def solution(num_list):
    str_odd = ''
    str_even = ''
    for i in num_list:
        if i % 2 == 0:
            str_even += str(i)
        else:
            str_odd += str(i)
    return int(str_even)+int(str_odd)