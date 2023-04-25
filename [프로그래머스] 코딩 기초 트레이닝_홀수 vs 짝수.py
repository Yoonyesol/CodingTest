def solution(num_list):
    odd = num_list[::2]
    even = num_list[1::2]
    return max(sum(odd), sum(even))