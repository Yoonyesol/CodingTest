def solution(array, height):
    return len([i for i in array if height < i])
