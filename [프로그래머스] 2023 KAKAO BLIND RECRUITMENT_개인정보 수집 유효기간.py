def solution(today, terms, privacies):
    answer = []
    fire = {i[0]:int(i[2:]) for i in terms}   #만료기간
    year, month, day = map(int, today.split("."))
    for i in range(len(privacies)):
        date, dtype = privacies[i].split()
        p_year, p_month, p_day = map(int, date.split("."))
        p_month += fire[dtype]
        while p_month > 12:
            p_month -= 12
            p_year += 1
        if year < p_year:
            continue
        elif year == p_year:
            if month < p_month:
                continue
            elif month == p_month:
                if day < p_day:
                    continue
        answer.append(i+1)
    return answer
