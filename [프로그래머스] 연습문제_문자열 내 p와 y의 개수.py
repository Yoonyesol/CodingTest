def solution(s):
    return False if s.count("p")+s.count("P")!=s.count("y")+s.count("Y") else True