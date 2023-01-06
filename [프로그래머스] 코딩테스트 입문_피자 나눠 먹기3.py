def solution(slice, n):
    return n // slice if n % slice == 0 else n // slice + 1