def solution(arr, query):
    for idx, qr in enumerate(query):
        if idx % 2 == 0:
            arr = arr[:qr+1]
        else:
            arr = arr[qr:]
    return arr