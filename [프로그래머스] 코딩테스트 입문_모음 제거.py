def solution(my_string):
    for i in ["a", "e", "i", "o", "u"]:
        if i in my_string:
            my_string = my_string.replace(i, "")
    return my_string