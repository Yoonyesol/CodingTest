def solution(n, lost, reserve):
    _res = list(set(reserve) - set(lost)) #여분 체육복이 있는 학생이 체육복을 도난당한 경우
    _lost = list(set(lost) - set(reserve)) #체육복을 도난당한 학생 중 여분 체육복을 가진 경우
    _res.sort(); #번호가 섞여있을 경우 체육복을 건네주는 순서가 엉키기 때문에 미리 정렬해준다.
    for i in _res:
        if i - 1 in _lost: #앞번호 학생에게 체육복을 빌려준 경우
            _lost.remove(i - 1) #체육복을 얻은 학생은 lost에서 제외시킨다.
        elif i + 1 in _lost: #뒷번호 학생에게 체육복을 빌려준 경우
            _lost.remove(i + 1)
    return n - len(_lost) #전체 학생 수에서 체육복을 얻지 못한 학생 수를 제외