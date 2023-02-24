def solution(polynomial):
    arr = polynomial.replace(" ", "").split("+")
    x, num = 0, 0
    for i in arr:
        if "x" in i:
            if len(i) >= 2:
                x += int(i[:-1])
            else:
                x += 1
        else:
            num += int(i)
    if num > 0 and x > 0:
        if x == 1:
            return "x + "+str(num)
        else:
            return str(x)+"x + "+str(num)
    elif x <= 0:
        return str(num)
    elif num <= 0:
        if x == 1:
            return "x"
        else:
            return str(x)+"x"