def solution(phone_number):
    pn = list(phone_number)
    for i in range(len(pn)-4):
        pn[i]="*"
    return ("".join(pn))