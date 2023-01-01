def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    else:
        answer = 0
        cities = [i.lower() for i in cities]
        stack = []
        for i in cities:
            if i not in stack:
                answer += 5
                if len(stack) == cacheSize:
                    stack.pop(0)
                stack.append(i)
            elif i in stack:
                stack.remove(i)
                stack.append(i)
                answer += 1
        return answer